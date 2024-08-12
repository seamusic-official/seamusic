from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.licenses import License
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.licenses.base import BaseLicensesRepository


@dataclass
class LicensesRepository(SQLAlchemyRepository, BaseLicensesRepository):
    async def get_user_licenses(self, user: dict) -> list[License]:
        query = select(License).filter_by(user=user)
        return list(await self.session.scalars(query))

    async def get_all_licenses(self) -> list[License]:
        query = select(License)
        return list(await self.session.scalars(query))

    async def get_license_by_id(self, license_id: int) -> License | None:
        return await self.session.get(License, license_id)

    async def add_license(self, license_: License) -> None:
        self.session.add(license_)

    async def update_license(self, license_: License) -> None:
        await self.session.merge(license_)

    async def delete_license(self, license_id: int, user_id: int) -> None:
        query = delete(License).where(License.id == license_id, License.user.id == user_id)
        await self.session.execute(query)
