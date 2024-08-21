from dataclasses import dataclass

from src.dtos.database.licenses import LicensesResponseDTO, CreateLicenseRequestDTO, UpdateLicenseRequestDTO
from src.exceptions.api import NoRightsException
from src.repositories import Repositories, DatabaseRepositories, BaseMediaRepository
from src.repositories.database.licenses.base import BaseLicensesRepository
from src.repositories.database.licenses.postgres import init_postgres_repository
from src.repositories.media.s3 import init_s3_repository


@dataclass
class LicensesDatabaseRepositories(DatabaseRepositories):
    licenses: BaseLicensesRepository


@dataclass
class LicensesRepositories(Repositories):
    database: LicensesDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class LicensesService:
    repositories: LicensesRepositories

    async def get_user_licenses(self, user_id: int) -> list[LicensesResponseDTO]:
        return await self.repositories.database.licenses.get_user_licenses(user_id=user_id)

    async def get_all_licenses(self) -> list[LicensesResponseDTO]:
        return await self.repositories.database.licenses.get_all_licenses()

    async def get_one(self, license_id: int) -> LicensesResponseDTO:
        return await self.repositories.database.licenses.get_license_by_id(license_id=license_id)

    async def add_license(
        self,
        title: str,
        description: str,
        price: str,
        user: dict
    ) -> int:

        license_ = CreateLicenseRequestDTO(
            title=title,
            description=description,
            price=price,
            user=user
        )

        return await self.repositories.database.licenses.add_license(license_=license_)

    async def update_license(
        self,
        license_id: int,
        user_id: int,
        title: str,
        description: str,
        price: str,
    ) -> None:

        license_ = await self.repositories.database.licenses.get_license_by_id(license_id=license_id)

        if license_.user.id != user_id:
            raise NoRightsException()

        license_ = UpdateLicenseRequestDTO(
            title=title,
            description=description,
            price=price
        )

        await self.repositories.database.licenses.update_license(license_=license_)

    async def delete_licenses(
        self,
        license_id: int,
        user_id: int
    ) -> None:

        license_ = await self.repositories.database.licenses.get_license_by_id(license_id=license_id)

        if license_.user.id != user_id:
            raise NoRightsException()

        await self.repositories.database.licenses.delete_license(license_id=license_id, user_id=user_id)


def get_licenses_service() -> LicensesService:
    return LicensesService(repositories=LicensesRepositories(
        database=LicensesDatabaseRepositories(licenses=init_postgres_repository()),
        media=init_s3_repository()
    ))
