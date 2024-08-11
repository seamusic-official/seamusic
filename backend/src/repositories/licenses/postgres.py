from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import select, delete

from src.models.licenses import License
from src.repositories.base import SQLAlchemyRepository
from src.repositories.licenses.base import BaseLicensesRepository


@dataclass
class LicensesRepository(SQLAlchemyRepository, BaseLicensesRepository):
    async def get_user_licenses(self, user: dict, **filter_by) -> Iterable[License]:
        query = select(License).filter_by(**filter_by)
        return await self._session.scalars(query)

    async def get_all_licenses(self) -> Iterable[License]:
        query = select(License)
        return await self._session.scalars(query)

    async def get_license_by_id(self, license_id: int) -> License | None:
        return await self._session.get(License, license_id)

    async def add_license(self, license_: License) -> None:
        self._session.add(license_)

    async def update_license(self, license_: License) -> None:
        await self._session.merge(license_)

    async def delete_license(self, license_id: int, user_id: int) -> None:
        query = delete(License).where(License.id == license_id, License.user.id == user_id)
        await self._session.execute(query)
