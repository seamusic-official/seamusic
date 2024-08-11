from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.soundkits import Soundkit
from src.repositories.base import SQLAlchemyRepository
from src.repositories.licenses.base import BaseLicensesRepository


@dataclass
class SounkitsReporitory(SQLAlchemyRepository, BaseLicensesRepository):
    async def get_user_soundkits(self, user_id: int) -> list[Soundkit]:
        query = select(Soundkit).filter_by(user_id=user_id)
        return list(await self._session.scalars(query))

    async def get_all_soundkits(self) -> list[Soundkit]:
        query = select(Soundkit)
        return list(await self._session.scalars(query))

    async def get_license_by_id(self, soundkit_id: int) -> Soundkit | None:
        return await self._session.get(Soundkit, soundkit_id)

    async def add_soundkit(self, soundkit: Soundkit) -> None:
        self._session.add(soundkit)

    async def update_license(self, soundkit: Soundkit) -> None:
        await self._session.merge(soundkit)

    async def delete_license(self, soundkit_id: int, user_id: int) -> None:
        query = delete(Soundkit).where(Soundkit.id == soundkit_id, Soundkit.user_id == user_id)
        await self._session.execute(query)
