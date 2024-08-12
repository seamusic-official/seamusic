from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.soundkits import Soundkit
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.soundkits.base import BaseSoundkitsRepository


@dataclass
class SounkitsReporitory(SQLAlchemyRepository, BaseSoundkitsRepository):
    async def get_user_soundkits(self, user_id: int) -> list[Soundkit]:
        query = select(Soundkit).filter_by(user_id=user_id)
        return list(await self.session.scalars(query))

    async def get_all_soundkits(self) -> list[Soundkit]:
        query = select(Soundkit)
        return list(await self.session.scalars(query))

    async def get_soundkit_by_id(self, soundkit_id: int) -> Soundkit | None:
        return await self.session.get(Soundkit, soundkit_id)

    async def add_soundkit(self, soundkit: Soundkit) -> None:
        self.session.add(soundkit)

    async def update_soundkit(self, soundkit: Soundkit) -> None:
        await self.session.merge(soundkit)

    async def delete_soundkit(self, soundkit_id: int, user_id: int) -> None:
        query = delete(Soundkit).where(Soundkit.id == soundkit_id, Soundkit.user_id == user_id)
        await self.session.execute(query)
