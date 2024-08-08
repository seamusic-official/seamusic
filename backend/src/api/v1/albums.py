from fastapi import UploadFile, File, APIRouter, Depends, status

from src.exceptions.api import NoRightsException
from src.core.media import MediaRepository
from src.schemas.albums import (
    Album,
    SAddAlbumResponse,
    SAlbumResponse,
    SAllAlbumsResponse,
    SDeleteAlbumResponse,
    SMyAlbumsResponse,
    SReleaseAlbumsRequest,
    SReleaseAlbumsResponse,
    SUpdateAlbumPictureResponse,
    SUpdateAlbumRequest,
    SUpdateAlbumResponse,
)
from src.services import albums as services
from src.schemas.auth import User
from src.repositories.albums import AlbumsRepository
from src.utils.auth import get_current_user
from src.utils.files import unique_filename, get_file_stream

albums = APIRouter(prefix="/albums", tags=["Albums"])


@albums.get(
    path="/my",
    summary="albums by current user",
    response_model=SMyAlbumsResponse,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SMyAlbumsResponse}},
)
async def get_my_albums(
    user: User = Depends(get_current_user),
) -> SMyAlbumsResponse:

    albums_ = await services.get_user_albums(user_id=user.id)
    albums_ = list(map(lambda album: Album.from_db_model(model=album), albums_))

    return SMyAlbumsResponse(albums=albums_)


@albums.get(
    path="/all",
    summary="Get all albums",
    response_model=Album,
    responses={status.HTTP_200_OK: {"model": Album}},
)
async def all_albums() -> Album:

    albums_ = await services.get_all_albums()
    # albums_ = list(map(lambda album: Album.from_db_model(model=album), albums_))
    album = albums_[0]
    return Album(
        id=album.id,
        created_at=album.created_at,
        updated_at=album.updated_at,
        is_available=album.is_available,
        title=album.name,
        picture_url=album.picture_url,
        description=album.description,
        co_prod=album.co_prod,
        type=album.type
    )
    return SAllAlbumsResponse(albums=albums_)


@albums.get(
    path="/get_one/{album_id}",
    summary="Get one album by id",
    response_model=SAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SAlbumResponse}},
)
async def get_one_album(album_id: int) -> SAlbumResponse:

    album = await services.get_one_album(album_id=album_id)
    return SAlbumResponse.from_db_model(model=album)


@albums.post(
    path="/add",
    summary="Init a album with file",
    response_model=SAddAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SAddAlbumResponse}},
)
async def add_album(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user)
) -> SAddAlbumResponse:
    file_info = unique_filename(file) if file else None

    album = await services.add_album(
        file_stream=await get_file_stream(file=file),
        file_info=file_info,
        prod_by=user.username,
        user_id=user.id
    )

    return SAddAlbumResponse.from_db_model(album)


@albums.post(
    path="/picture/{albums_id}",
    summary="Update a picture for one album by id",
    response_model=SUpdateAlbumPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateAlbumPictureResponse}},
)
async def update_album_picture(
    album_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user)
) -> SUpdateAlbumPictureResponse:
    album = await AlbumsRepository.find_one_by_id(id_=album_id)

    if album.user.id != user.id:
        raise NoRightsException()

    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)

    data = {"picture_url": file_url}

    response = await AlbumsRepository.edit_one(album_id, data)
    return SUpdateAlbumPictureResponse.from_db_model(model=response)


@albums.post(
    path="/release/{album_id}",
    summary="Release one album by id",
    response_model=SReleaseAlbumsResponse,
    responses={status.HTTP_200_OK: {"model": SReleaseAlbumsResponse}},
)
async def release_albums(
    album_id: int,
    albums_data: SReleaseAlbumsRequest,
    user: User = Depends(get_current_user),
) -> SReleaseAlbumsResponse:
    album = await AlbumsRepository.find_one_by_id(id_=album_id)

    if album.user.id != user.id:
        raise NoRightsException()

    data = {
        "name": albums_data.title,
        "description": albums_data.description,
        "co_prod": albums_data.co_prod,
    }

    response = await AlbumsRepository.edit_one(album_id, data)
    return SReleaseAlbumsResponse.from_db_model(model=response)


@albums.put(
    path="/update/{album_id}",
    summary="Edit album (title, description, prod_by) by id",
    response_model=SUpdateAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateAlbumResponse}},
)
async def update_album(
    album_id: int,
    albums_data: SUpdateAlbumRequest,
    user: User = Depends(get_current_user),
) -> SUpdateAlbumResponse:
    album = await AlbumsRepository.find_one_by_id(id_=album_id)

    if album.user.id != user.id:
        raise NoRightsException()

    data = {
        "name": albums_data.title,
        "description": albums_data.description,
        "prod_by": albums_data.prod_by,
    }

    response = await AlbumsRepository.edit_one(album_id, data)
    return SUpdateAlbumResponse.from_db_model(model=response)


@albums.delete(
    path="/delete/{album_id}",
    summary="Delete album by id",
    response_model=SDeleteAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteAlbumResponse}},
)
async def delete_albums(
    album_id: int, user: User = Depends(get_current_user)
) -> SDeleteAlbumResponse:
    album = await AlbumsRepository.find_one_by_id(id_=album_id)

    if album.user.id != user.id:
        raise NoRightsException()

    await AlbumsRepository.delete(id_=album_id)

    return SDeleteAlbumResponse()
