from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.tracks import Track
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.tracks.base import BaseTracksRepository


@dataclass
class TracksRepository(SQLAlchemyRepository, BaseTracksRepository):
    async def get_my_tracks(self, user_id: int) -> list[Track]:
        query = select(Track).filter_by(user_id=user_id)
        return list(await self.session.scalars(query))

    async def all_tracks(self) -> list[Track]:
        query = select(Track)
        return list(await self.session.scalars(query))

    async def get_one_track(self, track_id: int) -> Track | None:
        return await self.session.get(Track, track_id)

    async def update_track(self, data: dict) -> None:
        track = Track(**data)
        await self.session.merge(track)

    async def delete_track(self, track_id: int, user_id: int) -> None:
        query = delete(Track).where(Track.id == track_id, Track.user_id == user_id)
        await self.session.execute(query)
