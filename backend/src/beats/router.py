from src.beats.services import BeatsRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatUpdate, SBeatRelease
from src.beats.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.database  import get_async_session
from src.view.models import View
from src.auth.models import User
from .models import Beat
from datetime import datetime


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
async def get_one_beat(id: int, session: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_user)):

    detail = await session.execute(
        select(Beat).filter(Beat.id == id)
    )

    result_for_detail = detail.scalars().first()
    if not result_for_detail:
        raise HTTPException(detail='Beat Not Found', status_code=404)

    existing_view = await session.execute(
        select(View).filter(View.beats_id == id).filter(View.user_id == current_user.id)
    )

    result_for_existing_view = existing_view.scalars().first()
    if not result_for_existing_view:
        new_view = View(
            beats_id=id,
            user_id=current_user.id,
            is_available=True
        )

        session.add(new_view)
        result_for_detail.view_count = (result_for_detail.view_count or 0) + 1
        await session.commit()
        await session.refresh(new_view)

    return result_for_detail

from typing import List

@beats.get('/get-user-viewed-beats/', summary="Get beats viewed by the current user", response_model = List[SBeatBase])
async def get_user_viewed_beats(session: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_user)) -> List[Beat] | None:

    # Получение идентификаторов битов, которые пользователь просматривал
    viewed_beat_ids = await session.execute(
        select(View.beats_id).filter(View.user_id == current_user.id)
    )

    viewed_beat_ids_result = viewed_beat_ids.scalars().all()

    if not viewed_beat_ids_result:
        return []

    # Получение битов по идентификаторам, отсортированных по дате создания
    viewed_beats = await session.execute(
        select(Beat)
        .filter(Beat.id.in_(viewed_beat_ids_result))
        .order_by(Beat.created_at.desc())
    )

    viewed_beats_result = viewed_beats.scalars().all()

    return viewed_beats_result



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

