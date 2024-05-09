from src.beats.services import BeatsRepository, BeatPacksRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatPackBase, SBeatPack, SBeatPackCreate
from src.auth.schemas import SUser
from src.beats.utils import save_audio, save_image
from src.config import settings
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse

beats = APIRouter(
    prefix = "/beats",
    tags = ["Beats & Kits"]
)

@beats.get("/my", summary="Beats by current user")
async def get_user_beats(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(user=user)
    return response

@beats.get("/playlists/my", summary="Playlists by current user")
async def get_user_playlists(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(owner=user)
    return response

@beats.get("/likes/my", summary="Current user likes")
async def get_user_likes(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(owner=user)
    return response


@beats.post("/packs/my", summary="Packs by current user")
async def get_user_packs(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(owner=user)
    return response

@beats.post("/add", summary="Add a file for new beat")
async def add_beats(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await save_audio("MEDIA_BEATS", file) if file else None

    data = {
        "title": file_info['title'],
        "file_path": file_info['file_path'],
        "user_id": user.id
    }
    
    response = await BeatsRepository.add_one(data)
    return response

@beats.post("/picture/{beats_id}", summary="Update a picture for ur beats")
async def update_pic_beats(beats_id: int, picture_file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    picture_path = await save_image(settings.media.BEATS_PICTURES, picture_file) if picture_file else None
    data = {
        "picture": picture_path
    }
    print(data)
    response = await BeatsRepository.edit_one(beats_id, data)
    return response

@beats.post("/release/{id}", summary="Realise a beat")
async def release_beats(id: int, beats_data: SBeatBase):    
    data = {
        "title": beats_data["title"],
        "description": beats_data["description"],
        "co_prod": beats_data["co_prod"],
        "prod_by": beats_data["prod_by"],
    }

    await BeatsRepository.edit_one(id, data)
    return data

@beats.put("/update/{id}", summary="Create new beats")
async def update_beats(id: int, beats_data: SBeatBase):
    data = {
        "title": beats_data.title,
        "description": beats_data.description,
    }
    
    await BeatsRepository.edit_one(id, data)
    return data

@beats.delete("/delete/{id}", summary="Create new beats")
async def delete_beats(id: int):
    return await BeatsRepository.delete(id=id)

@beats.get("/all", summary="Create new beats")
async def all_beats():
    return await BeatsRepository.find_all()

@beats.get("/get_one/{id}", summary="Create new beats")
async def get_one(id: int):
    return await BeatsRepository.find_one_by_id(id)

import os
from pathlib import Path
from fastapi.responses import JSONResponse

base_dir = Path(__file__).resolve().parent.parent.parent / "MEDIA_BEATS"
print(base_dir)

@beats.get("/audio/{file_name}", summary="Get track with name")
async def get_audio(file_name: str):
    file_path = base_dir / file_name
    return file_path

@beats.get("/image/{file_name}", summary="Get image with name")
async def get_image(file_name: str):
    file_path = os.path.join(settings.media.BEATS_PICTURES, file_name)
    return FileResponse(file_path)

#BEATPACKS
@beats.post("/beatbacks/add", summary="Add a file for new beat")
async def add_beatpack(data: SBeatPackBase, user: SUser = Depends(get_current_user)):
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
    
    await BeatPacksRepository.edit_one(id, data)
    return data

@beats.delete("/beatpacks/delete/{id}", summary="Create new beats")
async def delete_beats(id: int):
    return await BeatPacksRepository.delete(id=id)

@beats.get("/beatpacks/all", summary="Create new beats")
async def all_beatpacks():
    return await BeatPacksRepository.find_all()

@beats.get("/beatpacks/{id}", summary="Create new beats")
async def get_one(id: int):
    return await BeatPacksRepository.find_one_by_id(id)