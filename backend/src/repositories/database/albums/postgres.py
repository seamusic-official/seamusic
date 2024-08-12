from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.albums import Album
from src.repositories.database.albums.base import BaseAlbumRepository
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class AlbumRepository(SQLAlchemyRepository, BaseAlbumRepository):
    async def create_album(self, album: Album) -> None:
        self.session.add(album)
        await self.session.flush()

    async def get_album_by_id(self, album_id: int) -> Album | None:
        return await self.session.get(Album, album_id)

    async def edit_album(self, album: Album) -> None:
        await self.session.merge(album)

    async def get_all_albums(self) -> list[Album]:
        query = select(Album)
        return list(await self.session.scalars(query))

    async def get_all_user_albums(self, user_id: int) -> list[Album]:
        query = select(Album).where(Album.user_id == user_id)
        return list(await self.session.scalars(query))

    async def delete_album(self, album_id: int, user_id: int) -> None:
        query = delete(Album).where(Album.id == album_id, Album.user_id == user_id)
        await self.session.execute(query)
