from src.soundkits.services import SoundkitService
from src.soundkits.schemas import SBeatBase, SBeat, SBeatCreate, SBeatpackBase, SBeatPack, SBeatPackCreate
from src.soundkits.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends


soundkits = APIRouter(
    prefix = "/soundkits",
    tags = ["Kits"]
)

#soundkits
@soundkits.get("/my", summary="soundkits by current user")
async def get_user_soundkits(user: SUser = Depends(get_current_user)):
    response = await soundkitsRepository.find_all(user=user)
    return response

@soundkits.get("/all", summary="Create new soundkits")
async def all_soundkits():
    return await soundkitsRepository.find_all()

@soundkits.get("/get_one/{id}", summary="Create new soundkits")
async def get_one_beat(id: int):
    return await soundkitsRepository.find_one_by_id(id)

@soundkits.post("/add", summary="Add a file for new beat")
async def add_soundkits(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_path = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_path": file_path,
        "prod_by": user.username,
        "user_id": user.id
    }

    response = await soundkitsRepository.add_one(data)
    return response

@soundkits.post("/picture/{soundkits_id}", summary="Update a picture for ur soundkits")
async def update_pic_soundkits(soundkits_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_path = await MediaRepository.upload_file("PICTURES", file_info, file)
    
    data = {
        "picture": file_path
    }
    
    response = await soundkitsRepository.edit_one(soundkits_id, data)
    return response

@soundkits.post("/release/{id}", summary="Realise a beat")
async def release_soundkits(id: int, soundkits_data: SBeatBase, user: SUser = Depends(get_current_user)):    
    data = {
        "title": soundkits_data.title ,
        "description": soundkits_data.description,
        "co_prod": soundkits_data.co_prod,
        "prod_by": soundkits_data.prod_by,
    }

    await soundkitsRepository.edit_one(id, data)
    return data

@soundkits.put("/update/{id}", summary="Create new soundkits")
async def update_soundkits(id: int, soundkits_data: SBeatBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": soundkits_data.title,
        "description": soundkits_data.description,
        "prod_by": soundkits_data.prod_by
    }
    
    await soundkitsRepository.edit_one(id, data)
    return data

@soundkits.delete("/delete/{id}", summary="Create new soundkits")
async def delete_soundkits(id: int):
    return await soundkitsRepository.delete(id=id)

#KITS
@soundkits.post("/my", summary="Packs by current user")
async def get_user_packs(user: SUser = Depends(get_current_user)):
    response = await soundkitsRepository.find_all(owner=user)
    return response

@soundkits.get("/all", summary="Create new soundkits")
async def all_beatpacks():
    return await BeatpacksRepository.find_all()

@soundkits.get("/{id}", summary="Create new soundkits")
async def get_one(id: int):
    return await BeatpacksRepository.find_one_by_id(id)

@soundkits.post("/add", summary="Add a file for new beat")
async def add_beatpack(data: SBeatpackBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "soundkits": data.soundkits
    }
    
    response = await soundkitsRepository.add_one(data)
    return response


@soundkits.post("/picture/{soundkits_id}", summary="Update a picture for ur soundkits")
async def update_pic_soundkits(soundkits_id: int, picture_file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    picture_path = await save_image(settings.media.soundkits_PICTURES, picture_file) if picture_file else None
    
    data = {
        "picture": picture_path
    }
    
    response = await soundkitsRepository.edit_one(soundkits_id, data)
    return response


@soundkits.put("/update/{id}", summary="Create new soundkits")
async def update_soundkits(id: int, soundkits_data: SBeatBase):
    data = {
        "title": soundkits_data.title,
        "description": soundkits_data.description,
    }
    
    await BeatpacksRepository.edit_one(id, data)
    return data

@soundkits.delete("/beatpacks/delete/{id}", summary="Create new soundkits")
async def delete_beatpackss(id: int):
    return await BeatpacksRepository.delete(id=id)


#BEATPACKS
@soundkits.post("/beatpacks/my", summary="Packs by current user")
async def get_user_packs(user: SUser = Depends(get_current_user)):
    response = await soundkitsRepository.find_all(owner=user)
    return response

@soundkits.get("/beatpacks/all", summary="Create new soundkits")
async def all_beatpacks():
    return await BeatpacksRepository.find_all()

@soundkits.get("/beatpacks/{id}", summary="Create new soundkits")
async def get_one(id: int):
    return await BeatpacksRepository.find_one_by_id(id)

@soundkits.post("/beatbacks/add", summary="Add a file for new beat")
async def add_beatpack(data: SBeatpackBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "soundkits": data.soundkits
    }
    
    response = await soundkitsRepository.add_one(data)
    return response

@soundkits.put("/beatpacks/update/{id}", summary="Create new soundkits")
async def update_soundkits(id: int, soundkits_data: SBeatBase):
    data = {
        "title": soundkits_data.title,
        "description": soundkits_data.description,
    }
    
    await BeatpacksRepository.edit_one(id, data)
    return data

@soundkits.delete("/beatpacks/delete/{id}", summary="Create new soundkits")
async def delete_beatpackss(id: int):
    return await BeatpacksRepository.delete(id=id)


@soundkits.get("/likes/my", summary="Current user likes")
async def get_user_likes(user: SUser = Depends(get_current_user)):
    response = await soundkitsRepository.find_all(owner=user)
    return response

