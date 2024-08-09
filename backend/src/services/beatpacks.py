from src.exceptions.api import NoRightsException
from src.models.beatpacks import Beatpack
from src.repositories.beatpacks import BeatpacksRepository
from src.schemas.auth import User


async def get_user_beatpacks(user: User) -> list[Beatpack]:
    return await BeatpacksRepository.find_all(owner=user)


async def all_beatpacks() -> list[Beatpack]:
    return await BeatpacksRepository.find_all()


async def get_one(beatpack_id: int) -> Beatpack:
    return await BeatpacksRepository.find_one_by_id(beatpack_id)


async def add_beatpack(
    title: str,
    description: str,
    beats: list[dict]
) -> Beatpack:

    data = {
        "title": title,
        "description": description,
        "beats": beats
    }

    return await BeatpacksRepository.add_one(data)


async def update_beatpacks(
    beatpack_id: int,
    user_id: int,
    title: str | None = None,
    description: str | None = None,
) -> None:

    beat_pack = await BeatpacksRepository.find_one_by_id(id_=beatpack_id)
    data = dict()

    if title:
        data["title"] = title
    if description:
        data["description"] = description

    for user_ in beat_pack.users:
        if user_id == user_.id:
            await BeatpacksRepository.edit_one(beatpack_id, data=data)
            return

    raise NoRightsException()


async def delete_beatpacks(
    beatpack_id: int,
    user_id: int
) -> None:
    beat_pack = await BeatpacksRepository.find_one_by_id(id_=beatpack_id)

    for user_ in beat_pack.users:
        if user_id == user_.id:
            await BeatpacksRepository.delete(id_=beatpack_id)
            return

    raise NoRightsException()
