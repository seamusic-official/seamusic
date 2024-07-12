from src.beats.services import BeatsRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatUpdate, SBeatRelease
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

@beats.get("", summary="Get all beats")
async def all_beats():
    return await BeatsRepository.find_all()

@beats.get("/{id}", summary="Get one beat by id")
async def get_one_beat(id: int):
    return await BeatsRepository.find_one_by_id(id)

@beats.post("", summary="Init a beat with file")
async def add_beats(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id,
        "type": "beat"
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
async def release_beats(id: int, data: SBeatRelease, user: SUser = Depends(get_current_user)):    
    update_data = {}

    if data.title:
        update_data["title"] = data.title
    if data.description:
        update_data["description"] = data.description
    if data.co_prod:
        update_data["co_prod"] = data.co_prod
    if data.prod_by:
        update_data["prod_by"] = data.prod_by
    
    await BeatsRepository.edit_one(id, update_data)
    return update_data


@beats.put("/{id}", summary="Create new beats")
async def update_beats(id: int, data: SBeatUpdate, user: SUser = Depends(get_current_user)):
    update_data = {}

    if data.title:
        update_data["title"] = data.title
    if data.description:
        update_data["description"] = data.description
    if data.picture_url:
        update_data["picture_url"] = data.picture_url
    if data.co_prod:
        update_data["co_prod"] = data.co_prod
    if data.prod_by:
        update_data["prod_by"] = data.prod_by
    
    await BeatsRepository.edit_one(id, update_data)
    return update_data

@beats.delete("/{id}", summary="Create new beats")
async def delete_beats(id: int):
    return await BeatsRepository.delete(id=id)

