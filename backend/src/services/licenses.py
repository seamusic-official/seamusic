from src.dtos.database.licenses import LicensesResponseDTO, CreateLicenseRequestDTO, UpdateLicenseRequestDTO
from src.exceptions.api import NoRightsException
from src.models.licenses import License


from src.repositories import Repositories
from src.repositories.database.licenses.base import BaseLicensesRepository


class SpotifyRepositories(Repositories):
    database: BaseLicensesRepository


class LicensesService:
    repositories: SpotifyRepositories


    async def get_user_licenses(self, user_id: int) -> list[LicensesResponseDTO]:
        return await self.repositories.database.get_user_licenses(user_id=user_id)


    async def get_all_licenses(self) -> list[LicensesResponseDTO]:
        return await self.repositories.database.get_all_licenses()


    async def get_one(self, license_id: int) -> LicensesResponseDTO:
        return await self.repositories.database.get_license_by_id(license_id=license_id)


    async def add_license(
        self,
        title: str,
        description: str,
        price: str,
        user: dict
    ) -> None:

        license_ = CreateLicenseRequestDTO(
            title=title,
            description=description,
            price=price,
            user=user
        )

        return await self.repositories.database.add_license(license_=license_)


    async def update_license(
        self,
        license_id: int,
        user_id: int,
        title: str,
        description: str,
        price: str,
    ) -> None:

        license_ = await self.repositories.database.get_license_by_id(license_id=license_id)

        if license_.user.id != user_id:
            raise NoRightsException()

        license = UpdateLicenseRequestDTO(
            title=title,
            description=description,
            price=price
        )


        await self.repositories.database.update_license(license_=license)


    async def delete_licenses(
        self,
        license_id: int,
        user_id: int
    ) -> None:

        license_ = await self.repositories.database.get_license_by_id(license_id=license_id)

        if license_.user.id != user_id:
            raise NoRightsException()

        await self.repositories.database.delete_license(license_id=license_id, user_id=user_id)
