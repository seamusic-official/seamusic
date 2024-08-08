from fastapi import UploadFile, File, APIRouter, Depends, status

from src.exceptions.api import NoRightsException
from src.core.media import MediaRepository
from src.schemas.auth import User
from src.schemas.beats import (
    SBeatResponse,
    SDeleteBeatResponse,
    SMyBeatsResponse,
    SBeatsResponse,
    SCreateBeatResponse,
    SUpdateBeatPictureResponse,
    SBeatReleaseRequest,
    SBeatReleaseResponse,
)
from src.schemas.beats import SBeatUpdateRequest, SBeatUpdateResponse
from src.repositories.beats import BeatsRepository
from src.utils.auth import get_current_user
from src.utils.files import unique_filename

beats = APIRouter(prefix="/beats", tags=["Beats"])


@beats.get(
    path="/my",
    summary="Beats by current user",
    status_code=status.HTTP_200_OK,
    response_model=SMyBeatsResponse,
    responses={status.HTTP_200_OK: {"model": SMyBeatsResponse}},
)
async def get_user_beats(user: User = Depends(get_current_user)) -> SMyBeatsResponse:
    response = await BeatsRepository.find_all(user=user)

    return SMyBeatsResponse(
        beats=[SBeatResponse.from_db_model(model=beat) for beat in response]
    )


@beats.get(
    path="/",
    summary="Get all beats",
    response_model=SBeatsResponse,
    responses={status.HTTP_200_OK: {"model": SBeatsResponse}},
)
async def all_beats() -> SBeatsResponse:
    response = await BeatsRepository.find_all()
    return SBeatsResponse(
        beats=[SBeatResponse.from_db_model(model=beat) for beat in response]
    )


@beats.get(
    path="/{beat_id}",
    summary="Get one beat by id",
    response_model=SBeatResponse,
    responses={status.HTTP_200_OK: {"model": SBeatResponse}},
)
async def get_one_beat(beat_id: int) -> SBeatResponse:
    response = await BeatsRepository.find_one_by_id(beat_id)
    return SBeatResponse.from_db_model(model=response)


@beats.post(
    path="/",
    summary="Init a beat with file",
    response_model=SCreateBeatResponse,
    responses={status.HTTP_200_OK: {"model": SCreateBeatResponse}},
)
async def add_beats(
    file: UploadFile = File(...), user: User = Depends(get_current_user)
) -> SCreateBeatResponse:
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)

    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id,
        "type": "beat",
    }

    response = await BeatsRepository.add_one(data)
    return SCreateBeatResponse.from_db_model(model=response)


@beats.put(
    path="/picture/{beat_id}",
    summary="Update a picture for one beat by id",
    response_model=SUpdateBeatPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateBeatPictureResponse}},
)
async def update_pic_beats(
    beat_id: int, file: UploadFile = File(...), user: User = Depends(get_current_user)
) -> SUpdateBeatPictureResponse:
    beat = await BeatsRepository.find_one_by_id(id_=beat_id)

    if beat.user_id != user.id:
        raise NoRightsException()

    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)

    data = {"picture_url": file_url}

    response = await BeatsRepository.edit_one(beat_id, data)
    return SUpdateBeatPictureResponse.from_db_model(model=response)


@beats.post(
    path="/release/{beat_id}",
    summary="Release one beat by id",
    response_model=SBeatReleaseResponse,
    responses={status.HTTP_200_OK: {"model": SBeatReleaseResponse}},
)
async def release_beats(
    beat_id: int, data: SBeatReleaseRequest, user: User = Depends(get_current_user)
) -> SBeatReleaseResponse:
    beat = await BeatsRepository.find_one_by_id(id_=beat_id)

    if beat.user_id != user.id:
        raise NoRightsException()

    update_data = {}

    if data.title:
        update_data["title"] = data.title
    if data.description:
        update_data["description"] = data.description
    if data.co_prod:
        update_data["co_prod"] = data.co_prod
    if data.prod_by:
        update_data["prod_by"] = data.prod_by

    response = await BeatsRepository.edit_one(beat_id, update_data)
    return SBeatReleaseResponse.from_db_model(model=response)


@beats.put(
    path="/{beat_id}",
    summary="Edit beat by id",
    response_model=SBeatUpdateResponse,
    responses={status.HTTP_200_OK: {"model": SBeatUpdateResponse}},
)
async def update_beats(
    beat_id: int, data: SBeatUpdateRequest, user: User = Depends(get_current_user)
) -> SBeatUpdateResponse:
    beat = await BeatsRepository.find_one_by_id(id_=beat_id)

    if beat.user_id != user.id:
        raise NoRightsException()

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

    response = await BeatsRepository.edit_one(beat_id, update_data)
    return SBeatUpdateResponse.from_db_model(model=response)


@beats.delete(
    path="/{beat_id}",
    summary="delete beat by id",
    response_model=SDeleteBeatResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteBeatResponse}},
)
async def delete_beats(
    beat_id: int, user: User = Depends(get_current_user)
) -> SDeleteBeatResponse:
    beat = await BeatsRepository.find_one_by_id(id_=beat_id)

    if beat.user_id != user.id:
        raise NoRightsException()

    await BeatsRepository.delete(id_=beat_id)
    return SDeleteBeatResponse()
