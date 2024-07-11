from src.soundkits.services import SoundkitRepository
from src.soundkits.schemas import SSoundkit, SSoundkitUpdate
from src.soundkits.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends
from typing import List

soundkits = APIRouter(
    prefix = "/soundkits",
    tags = ["Sound-kits"]
)

@soundkits.get("/my", summary="soundkits by current user")
async def get_user_soundkits(user: SUser = Depends(get_current_user)):
    response = await SoundkitRepository.find_all(user=user)
    return response

@soundkits.get("", summary="Get all soundkits")
async def all_soundkits():
    return await SoundkitRepository.find_all()

@soundkits.get("/{id}", summary="Get one soundkit by id")
async def get_one_soundkit(id: int):
    return await SoundkitRepository.find_one_by_id(id)

@soundkits.post("", summary="Init a soundkit with file")
async def add_soundkits(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id
    }

    response = await SoundkitRepository.add_one(data)
    return response

@soundkits.post("/picture/{soundkits_id}", summary="Update a picture for one soundkit by id")
async def update_pic_soundkits(soundkits_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)
    
    data = {
        "picture_url": file_url
    }
    
    response = await SoundkitRepository.edit_one(soundkits_id, data)
    return response

@soundkits.post("/release/{id}", summary="Release one soundkit by id")
async def release_soundkits(id: int, data: SSoundkitUpdate, user: SUser = Depends(get_current_user)):    
    update_data = {}

    if data.title:
        update_data["title"] = data.title
    if data.description:
        update_data["description"] = data.description
    if data.co_prod:
        update_data["co_prod"] = data.co_prod
    if data.prod_by:
        update_data["prod_by"] = data.prod_by
    
    await SoundkitRepository.edit_one(id, update_data)
    return update_data


@soundkits.put("/{id}", summary="Create new soundkits")
async def update_soundkits(id: int, data: SSoundkitUpdate, user: SUser = Depends(get_current_user)):
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
    
    await SoundkitRepository.edit_one(id, update_data)
    return update_data

@soundkits.delete("/{id}", summary="Create new soundkits")
async def delete_soundkits(id: int):
    return await SoundkitRepository.delete(id=id)

