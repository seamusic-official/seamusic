from dataclasses import dataclass


from src.exceptions.services import NotFoundException, NoRightsException
from src.models.beatpacks import Beatpack
from src.repositories.database.beatpacks.base import BaseBeatpacksRepository
from src.repositories.database.beatpacks.postgres import BeatpacksRepository


@dataclass
class BeatpackService:
    repository: BaseBeatpacksRepository

    async def get_user_beatpacks(self, user_id) -> list[Beatpack]:
        return await self.repository.get_user_beatpacks(user_id=user_id)

    async def get_all_beatpacks(self) -> list[Beatpack]:
        return await self.repository.get_all_beatpacks()

    async def get_one_beatpack(self, beatpack_id: int) -> Beatpack:
        beatpack = await self.repository.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        return beatpack

    async def add_beatpack(self, title: str, description: str) -> None:
        beatpack = Beatpack(
            title=title,
            description=description
        )

        return await self.repository.add_beatpack(beatpack=beatpack)

    async def update_beatpack(
            self,
            beatpack_id: int,
            user_id: int,
            title: str | None = None,
            description: str | None = None
    ) -> Beatpack:
        beatpack = await self.repository.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        for user in beatpack.users:
            if user.id == user_id:
                beatpack = Beatpack(
                    title=title if title else beatpack.title,
                    description=description if description else beatpack.description
                )
                return await self.repository.update_beatpack(beatpack=beatpack)

        raise NoRightsException()

    async def delete_beatpack(self, beatpack_id: int, user_id: int):
        beatpack = await self.repository.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        for user in beatpack.users:
            if user.id == user_id:

                return await self.repository.delete_beatpack(beatpack_id=beatpack_id)

        raise NoRightsException()


def init_beatpack_repository() -> BaseBeatpacksRepository:
    return BeatpacksRepository()

def get_beatpack_service() -> BeatpackService:
    repository = init_beatpack_repository()
    return BeatpackService(repository=repository)

