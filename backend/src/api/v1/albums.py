from fastapi import UploadFile, File, APIRouter, Depends, status

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

from src.schemas.auth import User
from src.services.albums import get_album_service, AlbumService

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
    service: AlbumService = Depends(get_album_service)
) -> SMyAlbumsResponse:

    albums_ = await service.get_user_albums(user_id=user.id)
    albums_ = list(map(lambda album: Album.from_db_model(model=album), albums_))

    return SMyAlbumsResponse(albums=albums_)


@albums.get(
    path="/all",
    summary="Get all albums",
    response_model=SAllAlbumsResponse,
    responses={status.HTTP_200_OK: {"model": SAllAlbumsResponse}},
)
async def all_albums(service: AlbumService = Depends(get_album_service)) -> SAllAlbumsResponse:

    albums_ = await service.get_all_albums()
    albums_ = list(map(lambda album: Album.from_db_model(model=album), albums_))

    return SAllAlbumsResponse(albums=albums_)


@albums.get(
    path="/get_one/{album_id}",
    summary="Get one album by id",
    response_model=SAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SAlbumResponse}},
)
async def get_one_album(
        album_id: int,
        service: AlbumService = Depends(get_album_service)
) -> SAlbumResponse:

    album = await service.get_one_album(album_id=album_id)
    return SAlbumResponse.from_db_model(model=album)


@albums.post(
    path="/add",
    summary="Init a album with file",
    response_model=SAddAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SAddAlbumResponse}},
)
async def add_album(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SAddAlbumResponse:
    file_info = unique_filename(file) if file else None

    album = await service.add_album(
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
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SUpdateAlbumPictureResponse:
    file_info = unique_filename(file) if file else None
    album = await service.update_album_picture(
        album_id=album_id,
        file_info=file_info,
        file_stream=get_file_stream(file),
        user_id=user.id
    )

    return SUpdateAlbumPictureResponse.from_db_model(model=album)


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
    service: AlbumService = Depends(get_album_service)
) -> SReleaseAlbumsResponse:
    album = await service.release_album(
        album_id=album_id,
        name=albums_data.name,
        description=albums_data.description,
        co_prod=albums_data.co_prod,
        user_id=user.id
    )
    return SReleaseAlbumsResponse.from_db_model(model=album)


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
    service: AlbumService = Depends(get_album_service)
) -> SUpdateAlbumResponse:
    album = await service.update_album(
        user_id=user.id,
        album_id=album_id,
        title=albums_data.title,
        description=albums_data.description,
        prod_by=albums_data.prod_by

    )
    return SUpdateAlbumResponse.from_db_model(model=album)


@albums.delete(
    path="/delete/{album_id}",
    summary="Delete album by id",
    response_model=SDeleteAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteAlbumResponse}},
)
async def delete_albums(
    album_id: int,
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SDeleteAlbumResponse:
    await service.delete_albums(album_id=album_id, user_id=user.id)

    return SDeleteAlbumResponse()
