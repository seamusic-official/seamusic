from sqlalchemy import select, delete

from src.models.beats import Beat
from src.repositories.converters.beats import convert_beat_db_query_result_to_dto
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.beats.base import BaseBeatsRepository
from src.repositories.dtos.beats import BeatDTO


class BeatsRepository(BaseBeatsRepository, SQLAlchemyRepository):
    async def get_user_beats(self, user_id: int) -> list[BeatDTO]:
        query = select(Beat).filter_by(user_id=user_id)
        beats = await self.session.scalars(query)

        return [convert_beat_db_query_result_to_dto(beat=beat) for beat in beats]

    async def all_beats(self) -> list[BeatDTO]:
        query = select(Beat)
        beats = await self.session.scalars(query)

        return [convert_beat_db_query_result_to_dto(beat=beat) for beat in beats]

    async def get_one_beat(self, beat_id: int) -> BeatDTO | None:
        beat = await self.session.get(Beat, beat_id)

        return convert_beat_db_query_result_to_dto(beat=beat)

    async def update_beat(self, data: dict) -> None:
        await self.session.merge(Beat(**data))

    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        query = delete(Beat).filter_by(beat_id=beat_id, user_id=user_id)
        await self.session.execute(query)
