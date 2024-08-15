from io import BytesIO

from src.repositories.media.base import S3Repository
from src.enums.type import Type
from src.exceptions.services import NoRightsException
from src.models.tracks import Track
from src.repositories.tracks import TracksRepository


class TracksService:
    @staticmethod
    async def get_my_tracks(user: dict) -> list[Track]:
        return await TracksRepository.find_all(user=user)

    @staticmethod
    async def all_tracks() -> list[Track]:
        return await TracksRepository.find_all()

    @staticmethod
    async def get_one_track(track_id: int) -> Track:
        return await TracksRepository.find_one_by_id(track_id)

    @staticmethod
    async def add_track(
        user: dict,
        file_info: str | None,
        file_stream: BytesIO
    ) -> Track:

        file_url = await S3Repository.upload_file("AUDIOFILES", file_info, file_stream)

        data = {
            "title": "Unknown title",
            "file_url": file_url,
            "prod_by": user["username"],
            "user_id": user["id"],
            "type": Type.track
        }

        return await TracksRepository.add_one(data)

    @staticmethod
    async def update_pic_tracks(
        track_id: int,
        user_id: int,
        file_info: str | None,
        file_stream: BytesIO,
    ) -> Track:

        track = await TracksRepository.find_one_by_id(id_=track_id)

        if track.id != user_id:
            raise NoRightsException()

        file_url = await S3Repository.upload_file("PICTURES", file_info, file_stream)
        data = {"picture_url": file_url}
        return await TracksRepository.edit_one(track_id, data)

    @staticmethod
    async def release_track(
        track_id: int,
        user_id: int,
        title: str,
        picture_url: str | None,
        description: str | None,
        co_prod: str | None,
        prod_by: str | None,
        playlist_id: int | None,
        track_pack_id: int | None,
    ) -> Track:

        track = await TracksRepository.find_one_by_id(id_=track_id)

        if track.id != user_id:
            raise NoRightsException()

        data = {
            "name": title,
            "description": description,
            "co_prod": co_prod,
            "prod_by": prod_by,
            "playlist_id": playlist_id,
            "picture_url": picture_url,
            "user_id": user_id,
            "track_pack_id": track_pack_id,
        }

        return await TracksRepository.edit_one(track_id, data)

    @staticmethod
    async def update_track(
        track_id: int,
        user_id: int,
        title: str,
        description: str | None,
        prod_by: str | None,
        picture: str | None,
        file_path: str,
        co_prod: str | None,
        playlist_id: int | None,
        track_pack_id: int | None,
    ) -> None:

        track = await TracksRepository.find_one_by_id(id_=track_id)

        if track.id != user_id:
            raise NoRightsException()

        data = {
            "name": title,
            "description": description,
            "prod_by": prod_by,
            "picture": picture,
            "file_path": file_path,
            "co_prod": co_prod,
            "playlist_id": playlist_id,
            "track_pack_id": track_pack_id
        }

        await TracksRepository.edit_one(track_id, data)

    @staticmethod
    async def delete_track(track_id: int, user_id: int) -> None:

        track = await TracksRepository.find_one_by_id(id_=track_id)

        if track.id != user_id:
            raise NoRightsException()

        await TracksRepository.delete(id_=track_id)
