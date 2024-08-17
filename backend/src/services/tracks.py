from io import BytesIO

from src.dtos.database.tracks import TracksResponseDTO, CreateTrackRequestDTO, UpdateTrackRequestDTO
from src.repositories import Repositories, BaseMediaRepository
from src.repositories.database.tracks.base import BaseTracksRepository


from src.exceptions.services import NoRightsException
from src.models.tracks import Track

class TrackRepositories(Repositories):
    database: BaseTracksRepository
    media: BaseMediaRepository

class TracksService:
    repositories: TrackRepositories


    async def get_my_tracks(self, user_id: int) -> list[TracksResponseDTO]:
        return await self.repositories.database.get_user_tracks(user_id=user_id)


    async def all_tracks(self) -> list[TracksResponseDTO]:
        return await self.repositories.database.get_all_tracks()


    async def get_one_track(self, track_id: int) -> TracksResponseDTO:
        return await self.repositories.database.get_track_by_id(track_id=track_id)


    async def add_track(
        self,
        username: str,
            track_title: str,
            description: str,
        user_id: int,
        file_info: str | None,
        file_stream: BytesIO
    ) -> Track:

        file_url = await self.repositories.media.upload_file("AUDIOFILES", file_info, file_stream)

        track = CreateTrackRequestDTO(
            title=track_title,
            description=description,
            file_path=file_url,
            prod_by=username,
            user_id=user_id
        )

        return await self.repositories.database.create_track(track=track)


    async def update_pic_tracks(
        self,
        track_id: int,
        user_id: int,
        file_info: str | None,
        file_stream: BytesIO,
    ) -> Track:
        file_url = await self.repositories.media.upload_file("PICTURES", file_info, file_stream)

        track = await self.repositories.database.get_track_by_id(track_id=track_id)

        if track.user_id != user_id:
            raise NoRightsException()

        track = UpdateTrackRequestDTO(
            title=track.name,
            file_path=file_url,
            user_id=user_id
        )
        return await self.repositories.database.update_track(track=track)


    async def release_track(
        self,
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

        track = await self.repositories.database.get_track_by_id(track_id=track_id)

        if track.user_id != user_id:
            raise NoRightsException()


        track = UpdateTrackRequestDTO(
            title=title,
            picture_url=picture_url,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            playlist_id=playlist_id,
            user_id=user_id,
            track_pack_id=track_pack_id
        )

        return await self.repositories.database.update_track(track=track)


    async def update_track(
        self,
        track_id: int,
        user_id: int,
        title: str,
        description: str | None,
        prod_by: str | None,
        picture_url: str | None,
        file_path: str,
        co_prod: str | None,
        playlist_id: int | None,
        track_pack_id: int | None,
    ) -> None:

        track = await self.repositories.database.get_track_by_id(track_id=track_id)

        if track.user_id != user_id:
            raise NoRightsException()

        track = UpdateTrackRequestDTO(
            title=title,
            picture_url=picture_url,
            file_path=file_path,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            playlist_id=playlist_id,
            user_id=user_id,
            track_pack_id=track_pack_id
        )

        await self.repositories.database.update_track(track=track)


    async def delete_track(self, track_id: int, user_id: int) -> None:
        track = await self.repositories.database.get_track_by_id(track_id=track_id)

        if track.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.delete_track(track_id=track_id, user_id=user_id)
