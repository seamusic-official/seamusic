from src.beatpacks.services import BeatpacksRepository
# from src.beatpacks.schemas import SBeatpackBase, SBeatPack, SBeatPackCreate
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user
from sqlalchemy import select
from .schemas import  BeatpackResponse, BeatpackCreate
from .models import Beatpack
from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.beats.models import Beat

from fastapi import UploadFile, File, APIRouter, Depends, HTTPException


beatpacks = APIRouter(
    prefix = "/beatpacks",
    tags = ["Beatpacks"]
)

@beatpacks.post("/my", summary="Packs by current user")
async def get_user_beatpacks(user: SUser = Depends(get_current_user)):
    response = await BeatpacksRepository.find_all(owner=user)
    return response

@beatpacks.get("/all", summary="Create new beatpacks")
async def all_beatpacks():
    return await BeatpacksRepository.find_all()

@beatpacks.get("/{id}", summary="Create new beatpacks")
async def get_one(id: int):
    return await BeatpacksRepository.find_one_by_id(id)


@beatpacks.post("/add", response_model=BeatpackResponse, summary="Add a new beatpack")
async def add_beatpack(
    data: BeatpackCreate, 
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user)
):
    new_beatpack = Beatpack(
        title=data.title,
        description=data.description
    )
    
    beat_ids = [beat.id for beat in data.beats]
    beats = await session.execute(select(Beat).where(Beat.id.in_(beat_ids)))
    new_beatpack.beats = beats.scalars().all()
    
    if not new_beatpack.beats:
        raise HTTPException(status_code=404, detail="No valid beats found")
    
    new_beatpack.user.append(current_user)
    
    session.add(new_beatpack)
    await session.commit()
    await session.refresh(new_beatpack)
    
    return BeatpackResponse.from_orm(new_beatpack)



# @beatpacks.put("/update/{id}", summary="Create new beatpacks")
# async def update_beatpacks(id: int, beatpacks_data: SBeatpackBase):
#     data = {
#         "title": beatpacks_data.title,
#         "description": beatpacks_data.description,
#     }
    
#     await BeatpacksRepository.edit_one(id, data)
#     return data

# @beatpacks.delete("/delete/{id}", summary="Create new beatpacks")
# async def delete_beatpacks(id: int):
#     return await BeatpacksRepository.delete(id=id)

