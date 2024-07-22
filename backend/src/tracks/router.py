from typing import List

from src.tracks.services import TracksRepository
from src.tracks.schemas import STrackBase, STrack, STrackCreate, STrackResponse, STrackUpdateResponse, \
    STrackDeleteResponse
from src.tracks.utils import unique_track_filename
from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user
from src.config import settings
from src.services import MediaRepository

from fastapi import UploadFile, File, APIRouter, Depends, status
from fastapi.responses import FileResponse


tracks = APIRouter(
    prefix = "/tracks",
    tags = ["Tracks"]
)

@tracks.get(
    "/my",
    summary="tracks by current user",
    response_model=List[STrackResponse],
    responses={
        status.HTTP_200_OK: {'model': List[STrackResponse]}
    }
)
async def get_user_tracks(user: SUser = Depends(get_current_user)) -> List[STrackResponse]:
    response = await TracksRepository.find_all(user=user)

    return [STrackResponse.from_db_model(track=track) for track in response]

@tracks.get(
    "/all",
    summary="Get all tracks",
    response_model=List[STrackResponse],
    responses={
        status.HTTP_200_OK: {'model': List[STrackResponse]}
    }
)
async def all_tracks() -> List[STrackResponse]:
    response = await TracksRepository.find_all()

    return [STrackResponse.from_db_model(track=track) for track in response]

@tracks.get(
    "/get_one/{id}",
    summary="Get one track by id",
    response_model=STrackResponse,
    responses={
        status.HTTP_200_OK: {'model': STrackResponse}
    }
)
async def get_one_track(id: int) -> STrackResponse:
    response = await TracksRepository.find_one_by_id(id)

    return STrackResponse.from_db_model(track=response)

@tracks.post(
    "/add",
    summary="Init a track with file",
    response_model=STrackResponse,
    responses={
        status.HTTP_200_OK: {'model': STrackResponse}
    }
)
async def add_tracks(
        file: UploadFile = File(...),
        user: SUser = Depends(get_current_user)
) -> STrackResponse:
    file_info = await unique_track_filename(file) if file else None

    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)

    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id,
        "type": "Track"
    }

    response = await TracksRepository.add_one(data)

    return STrackResponse.from_db_model(track=response)

@tracks.post(
    "/picture/{tracks_id}",
    summary="Update a picture for one track by id",
    response_model=STrackResponse,
    responses={
        status.HTTP_200_OK: {'model': STrackResponse}
    }
)
async def update_pic_tracks(
        tracks_id: int,
        file: UploadFile = File(...),
        user: SUser = Depends(get_current_user)
) -> STrackResponse:
    file_info = await unique_track_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)

    data = {
        "picture_url": file_url
    }
    
    response = await TracksRepository.edit_one(tracks_id, data)

    return STrackResponse.from_db_model(track=response)

@tracks.post(
    "/release/{id}",
    summary="Release one track by id",
    response_model=STrackResponse,
    responses={
        status.HTTP_200_OK: {'model': STrackResponse}
    }
)
async def release_tracks(
        id: int,
        tracks_data: STrackBase,
        user: SUser = Depends(get_current_user)
) -> STrackResponse:
    data = {
        "name": tracks_data.title ,
        "description": tracks_data.description,
        "co_prod": tracks_data.co_prod,
    }

    response = await TracksRepository.edit_one(id, data)

    return STrackResponse.from_db_model(track=response)

@tracks.put(
    "/update/{id}",
    summary="Edit track",
    response_model=STrackUpdateResponse,
    responses={
        status.HTTP_200_OK: {'model': STrackUpdateResponse}
    }
)
async def update_tracks(
        id: int,
        tracks_data: STrackBase,
        user: SUser = Depends(get_current_user)
) -> STrackUpdateResponse:
    data = {
        "name": tracks_data.title,
        "description": tracks_data.description,
        "prod_by": tracks_data.prod_by
    }
    
    await TracksRepository.edit_one(id, data)

    return STrackUpdateResponse

@tracks.delete(
    "/delete/{id}",
    summary="Delete track",
    response_model=STrackDeleteResponse,
    responses={
        status.HTTP_200_OK: {'model': STrackDeleteResponse}
    }
)
async def delete_tracks(id: int):
    await TracksRepository.delete(id=id)

    return STrackDeleteResponse

