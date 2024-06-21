from src.beatpacks.services import beatpacksRepository, BeatpacksRepository
from src.beatpacks.schemas import SBeatBase, SBeat, SBeatCreate, SBeatpackBase, SBeatPack, SBeatPackCreate
from src.beatpacks.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse


beatpacks = APIRouter(
    prefix = "/beatpacks",
    tags = ["Beatpacks"]
)

@beatpacks.post("/beatpacks/my", summary="Packs by current user")
async def get_user_beatpacks(user: SUser = Depends(get_current_user)):
    response = await beatpacksRepository.find_all(owner=user)
    return response

@beatpacks.get("/beatpacks/all", summary="Create new beatpacks")
async def all_beatpacks():
    return await BeatpacksRepository.find_all()

@beatpacks.get("/beatpacks/{id}", summary="Create new beatpacks")
async def get_one(id: int):
    return await BeatpacksRepository.find_one_by_id(id)

@beatpacks.post("/beatbacks/add", summary="Add a file for new beat")
async def add_beatpack(data: SBeatpackBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "beatpacks": data.beatpacks
    }
    
    response = await beatpacksRepository.add_one(data)
    return response

@beatpacks.put("/beatpacks/update/{id}", summary="Create new beatpacks")
async def update_beatpacks(id: int, beatpacks_data: SBeatBase):
    data = {
        "title": beatpacks_data.title,
        "description": beatpacks_data.description,
    }
    
    await BeatpacksRepository.edit_one(id, data)
    return data

@beatpacks.delete("/beatpacks/delete/{id}", summary="Create new beatpacks")
async def delete_beatpacks(id: int):
    return await BeatpacksRepository.delete(id=id)


@beatpacks.get("/likes/my", summary="Current user likes")
async def get_user_likes(user: SUser = Depends(get_current_user)):
    response = await beatpacksRepository.find_all(owner=user)
    return response

