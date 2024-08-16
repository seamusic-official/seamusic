from dataclasses import dataclass


from src.exceptions.services import NotFoundException, NoRightsException
from src.models.beatpacks import Beatpack
from src.repositories.beatpacks.base import BaseBeatpackRepository
from src.repositories.beatpacks.postgres import BeatpackRepository


@dataclass
class BeatpackService:
    respository: BaseBeatpackRepository

    async def get_user_beatpacks(self, user_id) -> list[Beatpack]:
        return await self.respository.get_all_user_beatpacks(user_id=user_id)

    async def get_all_beatpacks(self) -> list[Beatpack]:
        return await self.respository.get_all_beatpacks()

    async def get_one_beatpack(self, beatpack_id: int) -> Beatpack:
        beatpack = await self.respository.get_beatpack_by_id(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        return beatpack

    async def add_beatpack(self, title: str, description: str) -> None:
        beatpack = Beatpack(
            title=title,
            description=description
        )

        return await self.respository.create_beatpack(beatpack=beatpack)

    async def update_beatpack(
            self,
            beatpack_id: int,
            user_id: int,
            title: str | None = None,
            description: str | None = None
    ) -> Beatpack:
        beatpack = await self.respository.get_beatpack_by_id(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        for user in beatpack.users:
            if user.id == user_id:
                beatpack = Beatpack(
                    title=title if title else beatpack.title,
                    description=description if description else beatpack.description
                )
                return await self.respository.edit_beatpack(beatpack=beatpack)

        raise NoRightsException()

    async def delete_beatpack(self, beatpack_id: int, user_id: int):
        beatpack = await self.respository.get_beatpack_by_id(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        for user in beatpack.users:
            if user.id == user_id:

                return await self.respository.delete_beatpack(beatpack_id=beatpack_id)

        raise NoRightsException()


def init_beatpack_repository() -> BaseBeatpackRepository:
    return BeatpackRepository()

def get_beatpack_service() -> BeatpackService:
    repository = init_beatpack_repository()
    return BeatpackService(respository=repository)

