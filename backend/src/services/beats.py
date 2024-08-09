from io import BytesIO

from src.core.media import MediaRepository
from src.exceptions.services import NoRightsException
from src.models.beats import Beat
from src.repositories.beats import BeatsRepository


class BeatsService:
    @staticmethod
    async def get_user_beats(user: dict) -> list[Beat]:
        return await BeatsRepository.find_all(user=user)

    @staticmethod
    async def all_beats() -> list[Beat]:
        return await BeatsRepository.find_all()

    @staticmethod
    async def get_one_beat(beat_id: int) -> Beat:
        return await BeatsRepository.find_one_by_id(beat_id)

    @staticmethod
    async def add_beats(
            file_info: str | None,
            file_stream: BytesIO,
            user: dict
    ) -> Beat:
        file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file_stream)

        data = {
            "title": "Unknown title",
            "file_url": file_url,
            "prod_by": user["username"],
            "user_id": user["id"],
            "type": "beat",
        }

        return await BeatsRepository.add_one(data)

    @staticmethod
    async def update_pic_beats(
            beat_id: int,
            user_id: int,
            file_info: str | None,
            file_stream: BytesIO
    ) -> Beat:
        beat = await BeatsRepository.find_one_by_id(id_=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        file_url = await MediaRepository.upload_file("PICTURES", file_info, file_stream)

        data = {"picture_url": file_url}

        return await BeatsRepository.edit_one(beat_id, data)

    @staticmethod
    async def release_beats(
            beat_id: int,
            user_id: int,
            title: str | None,
            description: str | None,
            co_prod: str | None,
            prod_by: str | None
    ) -> Beat:
        beat = await BeatsRepository.find_one_by_id(id_=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        update_data = dict()

        if title:
            update_data["title"] = title
        if description:
            update_data["description"] = description
        if co_prod:
            update_data["co_prod"] = co_prod
        if prod_by:
            update_data["prod_by"] = prod_by

        return await BeatsRepository.edit_one(beat_id, update_data)

    @staticmethod
    async def update_beats(
            beat_id: int,
            user_id: int,
            title: str | None,
            description: str | None,
            picture_url: str | None,
            co_prod: str | None,
            prod_by: str | None
    ) -> Beat:
        beat = await BeatsRepository.find_one_by_id(id_=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        update_data = {}

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

        return await BeatsRepository.edit_one(beat_id, update_data)

    @staticmethod
    async def delete_beats(beat_id: int, user_id: int) -> None:
        beat = await BeatsRepository.find_one_by_id(id_=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        await BeatsRepository.delete(id_=beat_id)
