from typing import List

from fastapi import UploadFile, File, APIRouter, Depends, status

from src.beats.services import BeatsRepository
from src.beats.schemas import SBeatUpdate, SBeatRelease, SBeatResponse, SBeatDeleteResponse
from src.beats.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user


beats = APIRouter(
    prefix = "/beats",
    tags = ["Beats"]
)

@beats.get(
    "/my",
    summary="Beats by current user",
    response_model=List[SBeatResponse],
    responses={
        status.HTTP_200_OK: {'model': List[SBeatResponse]}
    }
)
async def get_user_beats(user: SUser = Depends(get_current_user)) -> List[SBeatResponse]:
    response = await BeatsRepository.find_all(user=user)

    return [SBeatResponse.from_db_model(beat=beat) for beat in response]

@beats.get(
    "",
    summary="Get all beats",
    response_model=List[SBeatResponse],
    responses={
        status.HTTP_200_OK: {'model': List[SBeatResponse]}
    }
)
async def all_beats() -> List[SBeatResponse]:
    response = await BeatsRepository.find_all()

    return [SBeatResponse.from_db_model(beat=beat) for beat in response]

@beats.get(
    "/{id}",
    summary="Get one beat by id",
    response_model=SBeatResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatResponse}
    }
)
async def get_one_beat(id: int) -> SBeatResponse:
    response = await BeatsRepository.find_one_by_id(id)

    return SBeatResponse.from_db_model(beat=response)

@beats.post(
    "",
    summary="Init a beat with file",
    response_model=SBeatResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatResponse}
    }
)
async def add_beats(
        file: UploadFile = File(...),
        user: SUser = Depends(get_current_user)
) -> SBeatResponse:
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

    return SBeatResponse.from_db_model(beat=response)

@beats.post(
    "/picture/{beats_id}",
    summary="Update a picture for one beat by id",
    response_model=SBeatResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatResponse}
    }
)
async def update_pic_beats(
        beats_id: int,
        file: UploadFile = File(...),
        user: SUser = Depends(get_current_user)
) -> SBeatResponse:
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)
    
    data = {
        "picture_url": file_url
    }
    
    response = await BeatsRepository.edit_one(beats_id, data)

    return SBeatResponse.from_db_model(beat=response)

@beats.post(
    "/release/{id}",
    summary="Release one beat by id",
    response_model=SBeatResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatResponse}
    }
)
async def release_beats(
        id: int,
        data: SBeatRelease,
        user: SUser = Depends(get_current_user)
) -> SBeatResponse:
    update_data = {}

    if data.title:
        update_data["title"] = data.title
    if data.description:
        update_data["description"] = data.description
    if data.co_prod:
        update_data["co_prod"] = data.co_prod
    if data.prod_by:
        update_data["prod_by"] = data.prod_by
    
    response = await BeatsRepository.edit_one(id, update_data)

    return SBeatResponse.from_db_model(beat=response)


@beats.put(
    "/{id}",
    summary="Edit beat by id",
    response_model=SBeatResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatResponse}
    }

)
async def update_beats(
        id: int,
        data: SBeatUpdate,
        user: SUser = Depends(get_current_user)
) -> SBeatResponse:
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
    
    response = await BeatsRepository.edit_one(id, update_data)

    return SBeatResponse.from_db_model(beat=response)

@beats.delete(
    "/{id}",
    summary="delete beat by id",
    response_model=SBeatDeleteResponse,
    responses={
        status.HTTP_200_OK: {'model': SBeatDeleteResponse}
    }
)
async def delete_beats(id: int, user: SUser = Depends(get_current_user)) -> SBeatDeleteResponse:
    await BeatsRepository.delete(id=id)

    return SBeatDeleteResponse

