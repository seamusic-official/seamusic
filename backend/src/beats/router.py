from src.beats.services import BeatsRepository, BeatpacksRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatpackBase, SBeatPack, SBeatPackCreate
from src.beats.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user
from sqlalchemy import Session
from src.database import get_db
from .models import Beat, View, chosen

from fastapi import UploadFile, File, APIRouter, Depends, HTTPException

from fastapi.responses import FileResponse
from datetime import datetime
from typing import List


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


@beats.get('/{id}/')
async def get_one_beat(
    id: int
):
    
    return await BeatsRepository.find_one_by_id(id=id)


@beats.get('/{id}/', summary="Get one beat", response_model=SBeatBase)
async def get_one_beat(
    id: int,
    current_user: SUser = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    beat = await SBeatBase.find_one_by_id(id=id)
    
    if not beat:
        raise HTTPException(status_code=404, detail="Not Found")

    exist_view = db.query(View).filter(
        View.beat_id == id,
        View.user_id == current_user.id
    ).first()


    if not exist_view:
        new_view = View(
            beat_id=id,
            user_id=current_user.id,
            timestap=datetime.utcnow()
        )
        db.add(new_view)
        db.commit()

        beat.view_count = (beat.view_count or 0) + 1
        db.commit()  

    return beat





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




@beats.get('/user/views', response_model=SBeatBase)
async def get_viewed_contents(
    db: Session = Depends(get_db),
    current_user: SUser = Depends(get_current_user)
):
    # Запрашиваем все просмотры текущего пользователя
    viewed_content_ids = db.query(View.beat_id).filter(
        View.user_id == current_user.id
    ).all()

    # Если пользователь не просмотрел ни одного контента
    if not viewed_content_ids:
        return []

    # Извлекаем контенты, которые пользователь просмотрел
    viewed_contents = db.query(Beat).filter(
        Beat.id.in_([vc[0] for vc in viewed_content_ids])
    ).all()