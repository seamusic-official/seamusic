from dataclasses import dataclass
from io import BytesIO

from src.dtos.database.auth import User
from src.dtos.database.beats import BeatsResponseDTO, CreateBeatRequestDTO, UpdateBeatRequestDTO
from src.enums.type import Type
from src.exceptions.services import NoRightsException
from src.models.beats import Beat
from src.repositories import DatabaseRepositories, Repositories
from src.repositories.database.beats.base import BaseBeatsRepository
from src.repositories.database.beats.postgres import init_postgres_repository
from src.repositories.media.base import BaseMediaRepository
from src.repositories.media.s3 import init_s3_repository
from src.services.base import BaseService


@dataclass
class BeatsDatabaseRepositories(DatabaseRepositories):
    beats: BaseBeatsRepository


@dataclass
class BeatsRepositories(Repositories):
    database: BeatsDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class BeatsService(BaseService):
    repositories: BeatsRepositories

    async def get_user_beats(self, user_id: int) -> BeatsResponseDTO:
        return await self.repositories.database.beats.get_user_beats(user_id=user_id)

    async def get_all_beats(self) -> BeatsResponseDTO:
        return await self.repositories.database.beats.all_beats()

    async def get_one_beat(self, beat_id: int) -> Beat:
        return await self.repositories.database.beats.get_one_beat(beat_id=beat_id)

    async def add_beats(
        self,
        file_info: str | None,
        file_stream: BytesIO,
        user: User
    ) -> int:

        file_url = await self.repositories.media.upload_file("AUDIOFILES", file_info, file_stream)

        beat = CreateBeatRequestDTO(
            title="Unknown title",
            description="",
            picture_url=None,
            file_url=file_url,
            co_prod=user.username,
            type=Type.beat,
            user_id=user.id
        )

        return await self.repositories.database.beats.create_beat(beat=beat)

    async def update_pic_beats(
        self,
        beat_id: int,
        user_id: int,
        file_info: str | None,
        file_stream: BytesIO
    ) -> int:

        beat = await self.repositories.database.beats.get_one_beat(beat_id=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        file_url = await self.repositories.media.upload_file("PICTURES", file_info, file_stream)
        beat = UpdateBeatRequestDTO(picture_url=file_url)
        return await self.repositories.database.beats.update_beat(beat=beat)

    async def release_beat(
        self,
        beat_id: int,
        user_id: int,
        title: str | None = None,
        description: str | None = None,
        co_prod: str | None = None,
        prod_by: str | None = None
    ) -> int:
        beat = await self.repositories.database.beats.get_one_beat(beat_id=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        beat = UpdateBeatRequestDTO(
            title=title,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            type=Type.beat,
            user_id=user_id
        )

        return await self.repositories.database.beats.update_beat(beat=beat)

    async def update_beat(
            self,
            beat_id: int,
            user_id: int,
            title: str | None = None,
            description: str | None = None,
            co_prod: str | None = None,
            prod_by: str | None = None
    ) -> int:
        beat = await self.repositories.database.beats.get_one_beat(beat_id=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        beat = UpdateBeatRequestDTO(
            title=title,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            type=Type.beat,
            user_id=user_id
        )

        return await self.repositories.database.beats.update_beat(beat=beat)

    async def delete_beats(self, beat_id: int, user_id: int) -> None:
        beat = await self.repositories.database.beats.get_one_beat(beat_id=beat_id)

        if beat.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.beats.delete_beat(beat_id=beat_id, user_id=user_id)


def get_beats_service() -> BeatsService:
    return BeatsService(repositories=BeatsRepositories(
        database=BeatsDatabaseRepositories(beats=init_postgres_repository()),
        media=init_s3_repository()
    ))
