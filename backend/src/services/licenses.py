from src.exceptions.api import NoRightsException
from src.models.licenses import License
from src.repositories.licenses import LicensesRepository


class LicensesService:
    @staticmethod
    async def get_user_licenses(user: dict) -> list[License]:
        return await LicensesRepository.find_all(owner=user)

    @staticmethod
    async def all_licenses() -> list[License]:
        return await LicensesRepository.find_all()

    @staticmethod
    async def get_one(license_id: int) -> License:
        return await LicensesRepository.find_one_by_id(int(license_id))

    @staticmethod
    async def add_license(
        title: str,
        description: str,
        price: str,
        user: dict
    ) -> License:

        data = {
            "title": title,
            "description": description,
            "price": price,
            "user": user
        }

        return await LicensesRepository.add_one(data=data)

    @staticmethod
    async def update_license(
        license_id: int,
        user_id: int,
        title: str,
        description: str,
        price: str,
    ) -> None:

        license_ = await LicensesRepository.find_one_by_id(id_=license_id)

        if license_.user.id != user_id:
            raise NoRightsException()

        data = dict()

        if title:
            data["title"] = title
        if description:
            data["description"] = description
        if price:
            data["price"] = price

        await LicensesRepository.edit_one(license_id, data)

    @staticmethod
    async def delete_licenses(
        license_id: int,
        user_id: int
    ) -> None:

        license_ = await LicensesRepository.find_one_by_id(id_=license_id)

        if license_.user.id != user_id:
            raise NoRightsException()

        await LicensesRepository.delete(id_=license_id)
