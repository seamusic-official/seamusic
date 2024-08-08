from fastapi import APIRouter, Depends, status

from src.exceptions.api import NoRightsException
from src.schemas.auth import User
from src.schemas.beatpacks import (
    SBeatpackResponse,
    SCreateBeatpackRequest,
    SEditBeatpackResponse,
    SDeleteBeatpackResponse,
    SMyBeatpacksResponse,
    Beatpack,
    SBeatpacksResponse,
    SCreateBeatpackResponse,
    SEditBeatpackRequest,
)
from src.repositories.beatpacks import BeatpacksRepository
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
) -> SMyBeatpacksResponse:

    response = await BeatpacksRepository.find_all(owner=user)
    from_db_model = lambda beatpack: Beatpack.from_db_model(model=beatpack)  # noqa: E731

    beatpacks_ = list(map(from_db_model, response))
    return SMyBeatpacksResponse(beatpacks=beatpacks_)


@beatpacks.get(
    path="/all",
    summary="Get all beat packs",
    response_model=SBeatpacksResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpacksResponse}},
)
async def all_beatpacks() -> SBeatpacksResponse:
    response = await BeatpacksRepository.find_all()
    return SBeatpacksResponse(
        beatpacks=[
            SBeatpackResponse.from_db_model(model=beatpack) for beatpack in response
        ]
    )


@beatpacks.get(
    path="/{beatpack_id}",
    summary="Get one beat pack by id",
    response_model=SBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def get_one(beatpack_id: int):
    response = await BeatpacksRepository.find_one_by_id(beatpack_id)
    return SBeatpackResponse.from_db_model(model=response)


@beatpacks.post(
    path="/add",
    summary="Add a file for new beat",
    response_model=SCreateBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SCreateBeatpackResponse}},
)
async def add_beatpack(data: SCreateBeatpackRequest) -> SCreateBeatpackResponse:
    response = await BeatpacksRepository.add_one(data.model_dump())
    return SCreateBeatpackResponse.from_db_model(model=response)


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
) -> SEditBeatpackResponse:
    beat_pack = await BeatpacksRepository.find_one_by_id(id_=beatpack_id)

    for user_ in beat_pack.users:
        if user.id == user_.id:
            await BeatpacksRepository.edit_one(beatpack_id, beatpacks_data.model_dump())
            return SEditBeatpackResponse()

    raise NoRightsException()


@beatpacks.delete(
    path="/delete/{beatpack_id}",
    summary="Delete beat pack",
    response_model=SDeleteBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteBeatpackResponse}},
)
async def delete_beatpacks(
    beatpack_id: int, user: User = Depends(get_current_user)
) -> SDeleteBeatpackResponse:
    beat_pack = await BeatpacksRepository.find_one_by_id(id_=beatpack_id)

    for user_ in beat_pack.users:
        if user.id == user_.id:
            await BeatpacksRepository.delete(id_=beatpack_id)
            return SDeleteBeatpackResponse()

    raise NoRightsException()
