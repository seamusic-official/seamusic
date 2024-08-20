from dataclasses import dataclass

from src.dtos.database.beatpacks import CreateBeatpackRequestDTO, UpdateBeatpackRequestDTO
from src.exceptions.services import NotFoundException, NoRightsException
from src.models.beatpacks import Beatpack
from src.repositories import DatabaseRepositories, Repositories
from src.repositories.database.beatpacks.base import BaseBeatpacksRepository
from src.repositories.database.beatpacks.postgres import init_postgres_repository
from src.repositories.media.s3 import S3Repository, init_s3_repository


@dataclass
class BeatpacksDatabaseRepositories(DatabaseRepositories):
    beatpacks: BaseBeatpacksRepository


@dataclass
class BeatpacksRepositories(Repositories):
    database: BeatpacksDatabaseRepositories
    media: S3Repository


@dataclass
class BeatpackService:
    respositories: BeatpacksRepositories

    async def get_user_beatpacks(self, user_id) -> list[Beatpack]:
        return await self.respositories.database.beatpacks.get_user_beatpacks(user_id=user_id)

    async def get_all_beatpacks(self) -> list[Beatpack]:
        return await self.respositories.database.beatpacks.get_all_beatpacks()

    async def get_one_beatpack(self, beatpack_id: int) -> Beatpack:
        beatpack = await self.respositories.database.beatpacks.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        return beatpack

    async def add_beatpack(self, title: str, description: str) -> int:
        beatpack = CreateBeatpackRequestDTO(
            title=title,
            description=description,
            beats=[]
        )

        return await self.respositories.database.beatpacks.add_beatpack(beatpack=beatpack)

    async def update_beatpack(
        self,
        beatpack_id: int,
        user_id: int,
        title: str | None = None,
        description: str | None = None
    ) -> int:
        beatpack = await self.respositories.database.beatpacks.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        for user in beatpack.users:
            if user.id == user_id:
                beatpack = UpdateBeatpackRequestDTO(
                    title=title if title else beatpack.title,
                    description=description if description else beatpack.description
                )
                return await self.respositories.database.beatpacks.update_beatpack(beatpack=beatpack)

        raise NoRightsException()

    async def delete_beatpack(self, beatpack_id: int, user_id: int):
        beatpack = await self.respositories.database.beatpacks.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        for user in beatpack.users:
            if user.id == user_id:
                return await self.respositories.database.beatpacks.delete_beatpack(beatpack_id=beatpack_id,
                                                                                   user_id=user_id)

        raise NoRightsException()


def get_beatpack_service() -> BeatpackService:
    return BeatpackService(respositories=BeatpacksRepositories(
        database=BeatpacksDatabaseRepositories(beatpacks=init_postgres_repository()),
        media=init_s3_repository()
    ))
