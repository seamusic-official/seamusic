from dataclasses import dataclass
from io import BytesIO

from src.dtos.database.albums import (
    Album,
    CreateAlbumRequestDTO,
    AlbumResponseDTO,
    UpdateAlbumRequestDTO,
    AlbumsResponseDTO
)
from src.enums.type import Type
from src.exceptions.services import NoRightsException, NotFoundException
from src.repositories import Repositories
from src.repositories.database.albums.base import BaseAlbumRepository
from src.repositories.database.albums.postgres import init_postgres_repository
from src.repositories.media.s3 import init_s3_repository, S3Repository
from src.services.base import BaseService


class AlbumRepositories(Repositories):
    database: BaseAlbumRepository
    media: S3Repository


@dataclass
class AlbumService(BaseService):

    repositories: AlbumRepositories

    async def get_user_albums(self, user_id: int) -> list[Album]:
        response: AlbumsResponseDTO = await self.repositories.database.get_user_albums(user_id=user_id)
        return response.albums

    async def get_all_albums(self) -> list[Album]:
        response: AlbumsResponseDTO = await self.repositories.database.get_all_albums()
        return response.albums

    async def get_one_album(self, album_id: int) -> Album:
        album: AlbumResponseDTO = await self.repositories.database.get_album_by_id(album_id=album_id)

        if album is None:
            raise NotFoundException(f"Album {album_id=} doesn't exist")

        return Album(**album.model_dump())

    async def add_album(
        self,
        title: str,
        description: str,
        file_stream: BytesIO,
        file_info: str,
        prod_by: str,
        user_id: int,
        co_prod: str | None = None,
    ) -> Album:

        file_url = await self.repositories.media.upload_file(
            folder="AUDIOFILES",
            filename=file_info,
            file_stream=file_stream
        )

        album = CreateAlbumRequestDTO(
            name=title,
            picture_url=file_url,
            description=description,
            prod_by=prod_by,
            co_prod=co_prod,
            type=Type.album,
            user_id=user_id
        )

        await self.repositories.database.create_album(album=album)
        return Album(**album.model_dump())

    async def update_album_picture(
        self,
        album_id: int,
        file_info: str | None,
        file_stream: BytesIO,
        user_id: int
    ) -> Album:

        album: AlbumResponseDTO = await self.repositories.database.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        await self.repositories.media.upload_file(
            folder="PICTURES",
            filename=file_info,
            file_stream=file_stream
        )
        return Album(**album.model_dump())

    async def release_album(
        self,
        album_id: int,
        name: str,
        description: str,
        co_prod: str,
        user_id: int,
    ) -> Album:

        album: AlbumResponseDTO = await self.repositories.database.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        updated_album = UpdateAlbumRequestDTO(
            name=name,
            picture_url=album.picture_url,
            description=description,
            co_prod=co_prod,
            type=Type.album,
            user_id=user_id
        )

        await self.repositories.database.edit_album(album=updated_album)
        return Album(**album.model_dump())

    async def update_album(
        self,
        user_id: int,
        album_id: int,
        title: str | None = None,
        co_prod: str | None = None,
        description: str | None = None,
    ) -> Album:

        album: AlbumResponseDTO = await self.repositories.database.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        updated_album = UpdateAlbumRequestDTO(
            name=title,
            picture_url=album.picture_url,
            description=description,
            co_prod=co_prod,
            type=Type.album,
            user_id=user_id
        )

        await self.repositories.database.edit_album(album=updated_album)
        return Album(**updated_album.model_dump())

    async def delete_album(self, album_id: int, user_id: int) -> None:
        album: AlbumResponseDTO = await self.repositories.database.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.delete_album(album_id=album_id, user_id=user_id)


def get_album_repositories() -> AlbumRepositories:
    return AlbumRepositories(database=init_postgres_repository(), media=init_s3_repository())


def get_album_service() -> AlbumService:
    return AlbumService(repositories=get_album_repositories())
