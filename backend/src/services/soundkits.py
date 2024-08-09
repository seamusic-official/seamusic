from io import BytesIO

from src.core.media import MediaRepository
from src.exceptions.api import NoRightsException
from src.models.soundkits import Soundkit
from src.repositories.soundkits import SoundkitRepository


class SoundkitsService:
    @staticmethod
    async def get_user_soundkits(user: dict) -> list[Soundkit]:
        return await SoundkitRepository.find_all(user=user)

    @staticmethod
    async def get_all_soundkits() -> list[Soundkit]:
        return await SoundkitRepository.find_all()

    @staticmethod
    async def get_one_soundkit(soundkit_id: int) -> Soundkit:
        return await SoundkitRepository.find_one_by_id(soundkit_id)

    @staticmethod
    async def add_soundkits(
        file_stream: BytesIO,
        file_info: str | None,
        user: dict
    ) -> Soundkit:

        file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file_stream)

        data = {
            "title": "Unknown title",
            "file_url": file_url,
            "prod_by": user["username"],
            "user_id": user["id"],
        }

        return await SoundkitRepository.add_one(data)

    @staticmethod
    async def update_pic_soundkits(
        soundkit_id: int,
        user_id: int,
        file_stream: BytesIO,
        file_info: str | None
    ) -> Soundkit:

        soundkit = await SoundkitRepository.find_one_by_id(id_=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        file_url = await MediaRepository.upload_file("PICTURES", file_info, file_stream)
        data = {"picture_url": file_url}
        return await SoundkitRepository.edit_one(soundkit_id, data)

    @staticmethod
    async def release_soundkits(
        soundkit_id: int,
        user_id: int,
        title: str | None,
        description: str | None,
        co_prod: str | None,
        prod_by: str | None
    ) -> Soundkit:

        soundkit = await SoundkitRepository.find_one_by_id(id_=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        update_data = {}

        if title:
            update_data["name"] = title
        if description:
            update_data["description"] = description
        if co_prod:
            update_data["co_prod"] = co_prod
        if prod_by:
            update_data["prod_by"] = prod_by

        return await SoundkitRepository.edit_one(soundkit_id, update_data)

    @staticmethod
    async def update_soundkits(
        soundkit_id: int,
        user_id: int,
        title: str | None,
        picture_url: str | None,
        description: str | None,
        co_prod: str | None,
        prod_by: str | None,
    ) -> Soundkit:

        soundkit = await SoundkitRepository.find_one_by_id(id_=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        update_data = dict()

        if title:
            update_data["title"] = title
        if description:
            update_data["description"] = description
        if picture_url:
            update_data["picture_url"] = picture_url
        if co_prod:
            update_data["co_prod"] = co_prod
        if prod_by:
            update_data["prod_by"] = prod_by

        return await SoundkitRepository.edit_one(soundkit_id, update_data)

    @staticmethod
    async def delete_soundkits(
        soundkit_id: int,
        user_id: int
    ) -> None:

        soundkit = await SoundkitRepository.find_one_by_id(id_=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        await SoundkitRepository.delete(id_=soundkit_id)
