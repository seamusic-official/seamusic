from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.auth import User
from src.models.beatpacks import Beatpack
from src.repositories.converters.beatpacks import convert_beatpack_db_query_result_to_dto
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.beatpacks.base import BaseBeatpacksRepository
from src.repositories.dtos.beatpacks import BeatpackDTO


@dataclass
class BeatpacksRepository(BaseBeatpacksRepository, SQLAlchemyRepository):
    async def get_user_beatpacks(self, user: dict) -> list[BeatpackDTO]:
        user = User(**user)
        query = select(Beatpack).where(user in Beatpack.users)
        beatpacks = await self.session.scalars(query)

        return [convert_beatpack_db_query_result_to_dto(beatpack=beatpack) for beatpack in beatpacks]

    async def get_all_beatpacks(self) -> list[BeatpackDTO]:
        query = select(Beatpack)
        beatpacks = await self.session.scalars(query)

        return [convert_beatpack_db_query_result_to_dto(beatpack=beatpack) for beatpack in beatpacks]

    async def get_one_beatpack(self, beatpack_id: int) -> BeatpackDTO | None:
        beatpack = await self.session.get(Beatpack, beatpack_id)

        return convert_beatpack_db_query_result_to_dto(beatpack=beatpack)

    async def add_beatpack(self, data: dict) -> None:
        self.session.add(Beatpack(**data))

    async def update_beatpack(self, data: dict) -> None:
        await self.session.merge(Beatpack(**data))

    async def delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
        query = delete(Beatpack).filter_by(beatpack_id=beatpack_id, user_id=user_id)
        await self.session.execute(query)
