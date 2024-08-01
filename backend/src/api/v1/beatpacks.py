from typing import List

from fastapi import APIRouter, Depends, status

from src.schemas.auth import SUser
from src.schemas.beatpacks import (
    BeatpackCreate,
    SBeatpackResponse,
    SBeatpackEditResponse,
    SBeatpackDeleteResponse,
)
from src.services.beatpacks import BeatpacksRepository
from src.utils.auth import get_current_user


beatpacks = APIRouter(prefix="/beatpacks", tags=["Beatpacks"])


@beatpacks.post(
    path="/my",
    summary="Get beat packs by current user",
    response_model=SBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def get_user_beatpacks(
    user: SUser = Depends(get_current_user),
) -> SBeatpackResponse:
    response = await BeatpacksRepository.find_all(owner=user)

    return SBeatpackResponse.from_db_model(beatpack=response)


@beatpacks.get(
    path="/all",
    summary="Get all beat packs",
    response_model=List[SBeatpackResponse],
    responses={status.HTTP_200_OK: {"model": List[SBeatpackResponse]}},
)
async def all_beatpacks() -> List[SBeatpackResponse]:
    response = await BeatpacksRepository.find_all()

    return [SBeatpackResponse.from_db_model(beatpack=beatpack) for beatpack in response]


@beatpacks.get(
    path="/{beatpack_id}",
    summary="Get one beat pack by id",
    response_model=SBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def get_one(beatpack_id: int):
    response = await BeatpacksRepository.find_one_by_id(beatpack_id)

    return SBeatpackResponse.from_db_model(beatpack=response)


@beatpacks.post(
    path="/add",
    summary="Add a file for new beat",
    response_model=SBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def add_beatpack(
    data: BeatpackCreate,
) -> SBeatpackResponse:
    data = {"title": data.title, "description": data.description, "beats": data.beats}

    response = await BeatpacksRepository.add_one(data)

    return SBeatpackResponse.from_db_model(beatpack=response)


@beatpacks.put(
    path="/update/{beatpack_id}",
    summary="Edit beat pack",
    response_model=SBeatpackEditResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def update_beatpacks(
    beatpack_id: int, beatpacks_data: BeatpackCreate
) -> SBeatpackEditResponse:
    data = {
        "title": beatpacks_data.title,
        "description": beatpacks_data.description,
    }

    await BeatpacksRepository.edit_one(beatpack_id, data)

    return SBeatpackEditResponse


@beatpacks.delete(
    path="/delete/{beatpack_id}",
    summary="Delete beat pack",
    response_model=SBeatpackDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackDeleteResponse}},
)
async def delete_beatpacks(beatpack_id: int) -> SBeatpackDeleteResponse:
    await BeatpacksRepository.delete(id_=beatpack_id)

    return SBeatpackDeleteResponse
