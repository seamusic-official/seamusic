from typing import List

from src.beatpacks.services import BeatpacksRepository
from src.beatpacks.schemas import SBeatpackBase, SBeatpackResponse, SBeatpackEditResponse, SBeatpackDeleteResponse
from src.auth.schemas import SUser

from src.auth.dependencies import get_current_user

from fastapi import APIRouter, Depends, status


beatpacks = APIRouter(
    prefix = "/beatpacks",
    tags = ["Beatpacks"]
)

@beatpacks.post(
    "/my",
    summary="Get beat packs by current user",
    response_model=SBeatpackResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatpackResponse}
    }
)
async def get_user_beatpacks(user: SUser = Depends(get_current_user)) -> SBeatpackResponse:
    response = await BeatpacksRepository.find_all(owner=user)

    return SBeatpackResponse.from_db_model(beatpack=response)

@beatpacks.get(
    "/all",
    summary="Get all beat packs",
    response_model=List[SBeatpackResponse],
    responses={
        status.HTTP_200_OK: {'model': List[SBeatpackResponse]}
    }
)
async def all_beatpacks() -> List[SBeatpackResponse]:
    response =  await BeatpacksRepository.find_all()

    return [SBeatpackResponse.from_db_model(beatpack=beatpack) for beatpack in response]

@beatpacks.get(
    "/{id}",
    summary="Get one beat pack by id",
    response_model=SBeatpackResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatpackResponse}
    }
)
async def get_one(id: int):
    response = await BeatpacksRepository.find_one_by_id(id)

    return SBeatpackResponse.from_db_model(beatpack=response)

@beatpacks.post(
    "/add",
    summary="Add a file for new beat",
    response_model=SBeatpackResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatpackResponse}
    }
)
async def add_beatpack(
        data: SBeatpackBase,
        user: SUser = Depends(get_current_user)
) -> SBeatpackResponse:
    data = {
        "title": data.title,
        "description": data.description,
        "beats": data.beats
    }
    
    response = await BeatpacksRepository.add_one(data)

    return SBeatpackResponse.from_db_model(beatpack=response)

@beatpacks.put(
    "/update/{id}",
    summary="Edit beat pack",
    response_model=SBeatpackEditResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatpackResponse}
    }

)
async def update_beatpacks(id: int, beatpacks_data: SBeatpackBase) -> SBeatpackEditResponse:
    data = {
        "title": beatpacks_data.title,
        "description": beatpacks_data.description,
    }
    
    await BeatpacksRepository.edit_one(id, data)

    return SBeatpackEditResponse

@beatpacks.delete(
    "/delete/{id}",
    summary="Delete beat pack",
    response_model=SBeatpackDeleteResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatpackDeleteResponse}
    }
)
async def delete_beatpacks(id: int) -> SBeatpackDeleteResponse:
    await BeatpacksRepository.delete(id=id)

    return SBeatpackDeleteResponse

