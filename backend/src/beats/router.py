from src.beats.services import BeatsRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate
from src.beats.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse


beats = APIRouter(
    prefix = "/beats",
    tags = ["Beats"]
)

@beats.get("/my", summary="Beats by current user")
async def get_user_beats(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(user=user)
    return response

@beats.get("/all", summary="Get all beats")
async def all_beats():
    return await BeatsRepository.find_all()

@beats.get("/get_one/{id}", summary="Get one beat by id")
async def get_one_beat(id: int):
    return await BeatsRepository.find_one_by_id(id)

@beats.post("/add", summary="Init a beat with file")
async def add_beats(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id
    }

    response = await BeatsRepository.add_one(data)
    return response

@beats.post("/picture/{beats_id}", summary="Update a picture for one beat by id")
async def update_pic_beats(beats_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)
    
    data = {
        "picture_url": file_url
    }
    
    response = await BeatsRepository.edit_one(beats_id, data)
    return response

@beats.post("/release/{id}", summary="Release one beat by id")
async def release_beats(id: int, beats_data: SBeatBase, user: SUser = Depends(get_current_user)):    
    data = {
        "title": beats_data.title ,
        "description": beats_data.description,
        "co_prod": beats_data.co_prod,
    }

    await BeatsRepository.edit_one(id, data)
    return data

@beats.put("/update/{id}", summary="Create new beats")
async def update_beats(id: int, beats_data: SBeatBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": beats_data.title,
        "description": beats_data.description,
        "prod_by": beats_data.prod_by
    }
    
    await BeatsRepository.edit_one(id, data)
    return data

@beats.delete("/delete/{id}", summary="Create new beats")
async def delete_beats(id: int):
    return await BeatsRepository.delete(id=id)

