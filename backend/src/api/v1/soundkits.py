from typing import List

from fastapi import UploadFile, File, APIRouter, Depends, status

from src.core.cruds import MediaRepository
from src.schemas.auth import SUser
from src.schemas.soundkits import (
    SSoundkitUpdate,
    SSoundkitResponse,
    SSoundkitDeleteResponse,
)
from src.services.soundkits import SoundkitRepository
from src.utils.auth import get_current_user
from src.utils.files import unique_filename


soundkits = APIRouter(prefix="/soundkits", tags=["Sound-kits"])


@soundkits.get(
    path="/my",
    summary="soundkits by current user",
    response_model=List[SSoundkitResponse],
    responses={status.HTTP_200_OK: {"model": List[SSoundkitResponse]}},
)
async def get_user_soundkits(
    user: SUser = Depends(get_current_user),
) -> List[SSoundkitResponse]:
    response = await SoundkitRepository.find_all(user=user)

    return [SSoundkitResponse.from_db_model(model=soundkit) for soundkit in response]


@soundkits.get(
    path="/",
    summary="Get all soundkits",
    response_model=List[SSoundkitResponse],
    responses={status.HTTP_200_OK: {"model": List[SSoundkitResponse]}},
)
async def all_soundkits() -> List[SSoundkitResponse]:
    response = await SoundkitRepository.find_all()
    return [SSoundkitResponse.from_db_model(model=soundkit) for soundkit in response]


@soundkits.get(
    path="/{soundkit_id}",
    summary="Get one soundkit by id",
    response_model=SSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitResponse}},
)
async def get_one_soundkit(soundkit_id: int) -> SSoundkitResponse:
    response = await SoundkitRepository.find_one_by_id(soundkit_id)
    return SSoundkitResponse.from_db_model(model=response)


@soundkits.post(
    path="/",
    summary="Init a soundkit with file",
    response_model=SSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitResponse}},
)
async def add_soundkits(
    file: UploadFile = File(...), user: SUser = Depends(get_current_user)
) -> SSoundkitResponse:
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)

    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id,
    }

    response = await SoundkitRepository.add_one(data)
    return SSoundkitResponse.from_db_model(model=response)


@soundkits.post(
    path="/picture/{soundkits_id}",
    summary="Update a picture for one soundkit by id",
    response_model=SSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitResponse}},
)
async def update_pic_soundkits(
    soundkits_id: int,
    file: UploadFile = File(...),
    user: SUser = Depends(get_current_user),
) -> SSoundkitResponse:
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)

    data = {"picture_url": file_url}

    response = await SoundkitRepository.edit_one(soundkits_id, data)
    return SSoundkitResponse.from_db_model(model=response)


@soundkits.post(
    path="/release/{soundkit_id}",
    summary="Release one soundkit by id",
    response_model=SSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitResponse}},
)
async def release_soundkits(
    soundkit_id: int, data: SSoundkitUpdate, user: SUser = Depends(get_current_user)
):
    update_data = {}

    if data.title:
        update_data["name"] = data.title
    if data.description:
        update_data["description"] = data.description
    if data.co_prod:
        update_data["co_prod"] = data.co_prod
    if data.prod_by:
        update_data["prod_by"] = data.prod_by

    response = await SoundkitRepository.edit_one(soundkit_id, update_data)

    return SSoundkitResponse.from_db_model(model=response)


@soundkits.put(
    path="/{soundkit_id}",
    summary="Edit soundkit",
    response_model=SSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitResponse}},
)
async def update_soundkits(
    soundkit_id: int, data: SSoundkitUpdate, user: SUser = Depends(get_current_user)
) -> SSoundkitResponse:
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

    response = await SoundkitRepository.edit_one(soundkit_id, update_data)
    return SSoundkitResponse.from_db_model(model=response)


@soundkits.delete(
    path="/{soundkit_id}",
    summary="Delete soundkit",
    response_model=SSoundkitDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitDeleteResponse}},
)
async def delete_soundkits(soundkit_id: int) -> SSoundkitDeleteResponse:
    await SoundkitRepository.delete(id_=soundkit_id)
    return SSoundkitDeleteResponse
