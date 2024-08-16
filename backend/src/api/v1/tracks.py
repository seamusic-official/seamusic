from fastapi import UploadFile, File, APIRouter, Depends, status

from src.dtos.database.tracks import Track
from src.exceptions.api import NoRightsException
from src.repositories.database.tracks.postgres import TracksRepository

from src.schemas.auth import User
from src.schemas.tracks import SMyTracksResponse, STrackResponse, SAddTracksResponse, SUpdateTrackPictureResponse, \
    SReleaseTrackResponse, SReleaseTrackRequest, SUpdateTrackResponse, SUpdateTrackRequest, SDeleteTrackResponse

from src.utils.auth import get_current_user
from src.utils.files import unique_filename

tracks = APIRouter(prefix="/tracks", tags=["Tracks"])


@tracks.get(
    path="/my",
    summary="tracks by current user",
    response_model=SMyTracksResponse,
    responses={status.HTTP_200_OK: {"model": SMyTracksResponse}},
)
async def get_my_tracks(
    user: User = Depends(get_current_user),
) -> SMyTracksResponse:
    response = TracksRepository.find_all(user=user)
    return SMyTracksResponse(
        tracks=[Track.from_db_model(model=track) for track in response]
    )


@tracks.get(
    path="/all",
    summary="Get all tracks",
    response_model=SMyTracksResponse,
    responses={status.HTTP_200_OK: {"model": SMyTracksResponse}},
)
async def all_tracks() -> SMyTracksResponse:
    response = TracksRepository.find_all()
    return SMyTracksResponse(
        tracks=[STrackResponse.from_db_model(model=track) for track in response]
    )


@tracks.get(
    path="/get_one/{track_id}",
    summary="Get one track by id",
    response_model=STrackResponse,
    responses={status.HTTP_200_OK: {"model": STrackResponse}},
)
async def get_one_track(track_id: int) -> STrackResponse:
    response = await TracksRepository.find_one_by_id(track_id)
    return STrackResponse.from_db_model(model=response)


@tracks.post(
    path="/add",
    summary="Init a track with file",
    response_model=SAddTracksResponse,
    responses={status.HTTP_200_OK: {"model": SAddTracksResponse}},
)
async def add_track(
    file: UploadFile = File(...), user: User = Depends(get_current_user)
) -> SAddTracksResponse:
    file_info = await unique_filename(file) if file else None

    file_url = await S3Repository.upload_file("AUDIOFILES", file_info, file)

    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id,
        "type": "Track",
    }

    response = await TracksRepository.add_one(data)
    return SAddTracksResponse.from_db_model(model=response)


@tracks.post(
    path="/picture/{tracks_id}",
    summary="Update a picture for one track by id",
    response_model=SUpdateTrackPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateTrackPictureResponse}},
)
async def update_pic_tracks(
    track_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
) -> SUpdateTrackPictureResponse:
    track = await TracksRepository.find_one_by_id(id_=track_id)

    if track.id != user.id:
        raise NoRightsException()

    file_info = await unique_filename(file) if file else None
    file_url = await S3Repository.upload_file("PICTURES", file_info, file)

    data = {"picture_url": file_url}

    response = await TracksRepository.edit_one(track_id, data)
    return SUpdateTrackPictureResponse.from_db_model(model=response)


@tracks.post(
    path="/release/{track_id}",
    summary="Release one track by id",
    response_model=SReleaseTrackResponse,
    responses={status.HTTP_200_OK: {"model": SReleaseTrackResponse}},
)
async def release_track(
    track_id: int,
    tracks_data: SReleaseTrackRequest,
    user: User = Depends(get_current_user),
) -> SReleaseTrackResponse:
    track = await TracksRepository.find_one_by_id(id_=track_id)

    if track.id != user.id:
        raise NoRightsException()

    data = {
        "name": tracks_data.title,
        "description": tracks_data.description,
        "co_prod": tracks_data.co_prod,
    }

    response = await TracksRepository.edit_one(track_id, data)
    return SReleaseTrackResponse.from_db_model(model=response)


@tracks.put(
    path="/update/{track_id}",
    summary="Edit track",
    response_model=SUpdateTrackResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateTrackResponse}},
)
async def update_track(
    track_id: int,
    tracks_data: SUpdateTrackRequest,
    user: User = Depends(get_current_user),
) -> SUpdateTrackResponse:
    track = await TracksRepository.find_one_by_id(id_=track_id)

    if track.id != user.id:
        raise NoRightsException()

    data = {
        "name": tracks_data.title,
        "description": tracks_data.description,
        "prod_by": tracks_data.prod_by,
    }

    await TracksRepository.edit_one(track_id, data)
    return SUpdateTrackResponse()


@tracks.delete(
    path="/delete/{track_id}",
    summary="Delete track",
    response_model=SDeleteTrackResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteTrackResponse}},
)
async def delete_tracks(track_id: int, user: User = Depends(get_current_user)):
    track = await TracksRepository.find_one_by_id(id_=track_id)

    if track.id != user.id:
        raise NoRightsException()

    await TracksRepository.delete(id_=track_id)
    return SDeleteTrackResponse()
