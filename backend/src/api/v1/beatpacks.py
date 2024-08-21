from fastapi import APIRouter, Depends, status

from src.schemas.auth import User
from src.schemas.beatpacks import (
    SBeatpackResponse,
    SCreateBeatpackRequest,
    SEditBeatpackResponse,
    SDeleteBeatpackResponse,
    SMyBeatpacksResponse,
    SBeatpacksResponse,
    SCreateBeatpackResponse,
    SEditBeatpackRequest,
)
from src.services.beatpacks import BeatpackService, get_beatpack_service
from src.utils.auth import get_current_user

beatpacks = APIRouter(prefix="/beatpacks", tags=["Beatpacks"])


@beatpacks.post(
    path="/my",
    summary="Get beat packs by current user",
    response_model=SMyBeatpacksResponse,
    responses={status.HTTP_200_OK: {"model": SMyBeatpacksResponse}},
)
async def get_user_beatpacks(
    user: User = Depends(get_current_user),
    service: BeatpackService = Depends(get_beatpack_service)
) -> SMyBeatpacksResponse:
    beatpacks = await service.get_user_beatpacks(user_id=user.id)

    return SMyBeatpacksResponse(beatpacks=beatpacks)


@beatpacks.get(
    path="/all",
    summary="Get all beat packs",
    response_model=SBeatpacksResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpacksResponse}},
)
async def all_beatpacks(service: BeatpackService = Depends(get_beatpack_service)) -> SBeatpacksResponse:
    beatpacks = await service.get_all_beatpacks()
    return SBeatpacksResponse(
        beatpacks=[
            SBeatpackResponse.from_db_model(model=beatpack) for beatpack in beatpacks
        ]
    )


@beatpacks.get(
    path="/{beatpack_id}",
    summary="Get one beat pack by id",
    response_model=SBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def get_one(
        beatpack_id: int,
        service: BeatpackService = Depends(get_beatpack_service)
):
    beatpack = await service.get_one_beatpack(beatpack_id=beatpack_id)

    return SBeatpackResponse.from_db_model(model=beatpack)


@beatpacks.post(
    path="/add",
    summary="Add a file for new beat",
    response_model=SCreateBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SCreateBeatpackResponse}},
)
async def add_beatpack(
        data: SCreateBeatpackRequest,
        service: BeatpackService = Depends(get_beatpack_service)
) -> SCreateBeatpackResponse:
    beatpack = await service.add_beatpack(
        title=data.title,
        description=data.description
    )
    return SCreateBeatpackResponse.from_db_model(model=beatpack)


@beatpacks.put(
    path="/update/{beatpack_id}",
    summary="Edit beat pack",
    response_model=SEditBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SEditBeatpackResponse}},
)
async def update_beatpacks(
    beatpack_id: int,
    beatpacks_data: SEditBeatpackRequest,
    user: User = Depends(get_current_user),
    service: BeatpackService = Depends(get_beatpack_service)
) -> SEditBeatpackResponse:
    beatpack = await service.update_beatpack(
        beatpack_id=beatpack_id,
        user_id=user.id,
        title=beatpacks_data.title,
        description=beatpacks_data.description
    )

    return SEditBeatpackResponse()



@beatpacks.delete(
    path="/delete/{beatpack_id}",
    summary="Delete beat pack",
    response_model=SDeleteBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteBeatpackResponse}},
)
async def delete_beatpacks(
    beatpack_id: int,
    user: User = Depends(get_current_user),
    service: BeatpackService = Depends(get_beatpack_service)
) -> SDeleteBeatpackResponse:
    await service.delete_beatpack(
        beatpack_id=beatpack_id,
        user_id=user.id
    )
    return SDeleteBeatpackResponse()

