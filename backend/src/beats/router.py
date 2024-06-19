from src.beats.services import BeatsRepository, BeatpacksRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatpackBase, SBeatPack, SBeatPackCreate
from src.beats.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse


beats = APIRouter(
    prefix = "/beats",
    tags = ["Beats & Kits & Beatpacks"]
)

#BEATS
@beats.get("/my", summary="Beats by current user")
async def get_user_beats(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(user=user)
    return response

@beats.get("/all", summary="Create new beats")
async def all_beats():
    return await BeatsRepository.find_all()

@beats.get("/get_one/{id}", summary="Create new beats")
async def get_one_beat(id: int):
    return await BeatsRepository.find_one_by_id(id)

@beats.post("/add", summary="Add a file for new beat")
async def add_beats(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_path = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_path": file_path,
        "prod_by": user.username,
        "user_id": user.id
    }

    response = await BeatsRepository.add_one(data)
    return response

@beats.post("/picture/{beats_id}", summary="Update a picture for ur beats")
async def update_pic_beats(beats_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_path = await MediaRepository.upload_file("PICTURES", file_info, file)
    
    data = {
        "picture": file_path
    }
    
    response = await BeatsRepository.edit_one(beats_id, data)
    return response

@beats.post("/release/{id}", summary="Realise a beat")
async def release_beats(id: int, beats_data: SBeatBase, user: SUser = Depends(get_current_user)):    
    data = {
        "title": beats_data.title ,
        "description": beats_data.description,
        "co_prod": beats_data.co_prod,
        "prod_by": beats_data.prod_by,
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

#KITS
@beats.post("/my", summary="Packs by current user")
async def get_user_packs(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(owner=user)
    return response

@beats.get("/all", summary="Create new beats")
async def all_beatpacks():
    return await BeatpacksRepository.find_all()

@beats.get("/{id}", summary="Create new beats")
async def get_one(id: int):
    return await BeatpacksRepository.find_one_by_id(id)

@beats.post("/add", summary="Add a file for new beat")
async def add_beatpack(data: SBeatpackBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "beats": data.beats
    }
    
    response = await BeatsRepository.add_one(data)
    return response


@beats.post("/picture/{beats_id}", summary="Update a picture for ur beats")
async def update_pic_beats(beats_id: int, picture_file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    picture_path = await save_image(settings.media.BEATS_PICTURES, picture_file) if picture_file else None
    
    data = {
        "picture": picture_path
    }
    
    response = await BeatsRepository.edit_one(beats_id, data)
    return response


@beats.put("/update/{id}", summary="Create new beats")
async def update_beats(id: int, beats_data: SBeatBase):
    data = {
        "title": beats_data.title,
        "description": beats_data.description,
    }
    
    await BeatpacksRepository.edit_one(id, data)
    return data

@beats.delete("/beatpacks/delete/{id}", summary="Create new beats")
async def delete_beatpackss(id: int):
    return await BeatpacksRepository.delete(id=id)


#BEATPACKS
@beats.post("/beatpacks/my", summary="Packs by current user")
async def get_user_packs(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(owner=user)
    return response

@beats.get("/beatpacks/all", summary="Create new beats")
async def all_beatpacks():
    return await BeatpacksRepository.find_all()

@beats.get("/beatpacks/{id}", summary="Create new beats")
async def get_one(id: int):
    return await BeatpacksRepository.find_one_by_id(id)

@beats.post("/beatbacks/add", summary="Add a file for new beat")
async def add_beatpack(data: SBeatpackBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "beats": data.beats
    }
    
    response = await BeatsRepository.add_one(data)
    return response

@beats.put("/beatpacks/update/{id}", summary="Create new beats")
async def update_beats(id: int, beats_data: SBeatBase):
    data = {
        "title": beats_data.title,
        "description": beats_data.description,
    }
    
    await BeatpacksRepository.edit_one(id, data)
    return data

@beats.delete("/beatpacks/delete/{id}", summary="Create new beats")
async def delete_beatpackss(id: int):
    return await BeatpacksRepository.delete(id=id)


@beats.get("/likes/my", summary="Current user likes")
async def get_user_likes(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(owner=user)
    return response

