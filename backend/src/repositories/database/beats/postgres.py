from sqlalchemy import select, delete

from src.models.beats import Beat
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.beats.base import BaseBeatsRepository


class BeatsRepository(BaseBeatsRepository, SQLAlchemyRepository):
    async def get_user_beats(self, user_id: int) -> list[Beat]:
        query = select(Beat).filter_by(user_id=user_id)
        return list(await self.session.scalars(query))

    async def all_beats(self) -> list[Beat]:
        query = select(Beat)
        return list(await self.session.scalars(query))

    async def get_one_beat(self, beat_id: int) -> Beat | None:
        return await self.session.get(Beat, beat_id)

    async def update_beat(self, data: dict) -> None:
        await self.session.merge(Beat(**data))

    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        query = delete(Beat).filter_by(beat_id=beat_id, user_id=user_id)
        await self.session.execute(query)
