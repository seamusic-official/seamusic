from dataclasses import dataclass

from io import BytesIO

from src.core.database import get_async_session
from src.core.media import MediaRepository
from src.exceptions.services import NoRightsException
from src.models.albums import Album
from src.repositories.albums.album import AlbumRepository
from src.repositories.albums.base import BaseAlbumRepository


@dataclass
class AlbumService:
    repository: BaseAlbumRepository

    async def get_user_albums(self, user_id: int) -> list[Album]:
        return await self.repository.get_all_user_albums(user_id=user_id)

    async def get_all_albums(self) -> list[Album]:
        albums = await self.repository.get_all_albums()

        albums_ = []

        for album in albums:
            albums_.append(album)

        return albums_


    async def get_one_album(self, album_id: int) -> Album:
        return await self.repository.get_album_by_id(album_id=album_id)


    async def add_album(
        self,
        title: str,
        description: str,
        file_stream: BytesIO,
        file_info: str | None,
        prod_by: str,
        user_id: int,
    ) -> Album:
    
        file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file_stream)

        album = Album(
            name=title,
            picture_url=file_url,
            description=description,
            co_prod=prod_by,
            type="album",
            user_id=user_id
        )

        return await self.repository.create_album(album=album)


    async def update_album_picture(
        self,
        album_id: int,
        file_info: str | None,
        file_stream: BytesIO,
        user_id: int
    ) -> Album:
    
        album = await self.repository.get_album_by_id(album_id=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()
    
        file_url = await MediaRepository.upload_file("PICTURES", file_info, file_stream)

        _album = Album(
            name=album.name,
            picture_url=file_url,
            description=album.description,
            co_prod=album.co_prod,
            type=album.type,
            user_id=album.user_id
        )
    
        return await self.repository.edit_album(album=_album)

    async def release_album(
        self,
        album_id: int,
        name: str,
        description: str,
        co_prod: str,
        user_id: int,
    ) -> Album:
        album = await self.repository.get_album_by_id(album_id=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()

        _album = Album(
            name=name,
            picture_url=album.picture_url,
            description=description,
            co_prod=co_prod,
            type=album.type,
            user_id=album.user_id
        )
    
        return await self.repository.edit_album(album=_album)

    async def update_album(
        self,
        user_id: int,
        album_id: int,
        title: str | None,
        description: str | None,
        prod_by: str | None,
    ) -> Album:
    
        album = await self.repository.get_album_by_id(album_id=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()

        _album = Album(
            name=title,
            picture_url=album.picture_url,
            description=description,
            co_prod=prod_by,
            type=album.type,
            user_id=album.user_id
        )

        return await self.repository.edit_album(album=_album)

    async def delete_albums(self, album_id: int, user_id: int) -> None:
        album = await self.repository.get_album_by_id(album_id=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()
    
        await self.repository.delete_album(album_id=album_id, user_id=user_id)

async def init_album_repository() -> BaseAlbumRepository:
        async for session in get_async_session():
            return AlbumRepository(_session=session)

async def get_album_service() -> AlbumService:
    repository = await init_album_repository()
    return AlbumService(repository=repository)