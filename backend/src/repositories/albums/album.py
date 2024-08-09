from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import select, delete

from src.models.albums import Album
from src.repositories.base import SQLAlchemyRepository
from src.repositories.albums.base import BaseAlbumRepository


@dataclass
class AlbumRepository(SQLAlchemyRepository, BaseAlbumRepository):
    async def create_album(self, album: Album) -> None:
        self._session.add(album)
        await self._session.flush()


    async def get_album_by_id(self, album_id: int) -> Album:
        album: Album = await self._session.get(Album, album_id)

        return album

    async def edit_album(self, album: Album) -> Album:
        await self._session.merge(album)

    async def get_all_albums(self) -> Iterable[Album]:
        query = select(Album)
        result: Iterable[Album] = await self._session.scalars(query)

        return result

    async def get_all_user_albums(self, user_id: int) -> Iterable[Album]:
        query = select(Album).where(Album.user_id == user_id)
        result: Iterable[Album] = await self._session.scalars(query)

        return result

    async def delete_album(self, album_id: int,user_id: int) -> None:
        query = delete(Album).where(Album.id == album_id, Album.user_id == user_id)

        await self._session.execute(query)
        await self._session.commit()