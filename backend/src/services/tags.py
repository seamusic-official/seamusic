from src.exceptions.services import NotFoundException
from src.models.tags import Tag
from src.repositories.auth import ProducerDAO, ArtistDAO
from src.repositories.tags import ListenerTagsDAO, ProducerTagsDAO, ArtistTagsDAO, TagsDAO


class TagsService:
    @staticmethod
    async def add_tag(name: str) -> Tag:
        return await TagsDAO.add_one({"name": name})

    @staticmethod
    async def get_my_listener_tags(
        user: dict
    ) -> list[Tag]:
        return await ListenerTagsDAO.find_all(listener_profile=user)

    @staticmethod
    async def get_my_producer_tags(user: dict) -> list[Tag]:
        producer_profile = await ProducerDAO.find_one_or_none(producer_profile=user)

        if not producer_profile:
            raise NotFoundException("You don't have a producer profile")

        return await ProducerTagsDAO.find_all(producer_profile=producer_profile)

    @staticmethod
    async def get_my_artist_tags(user: dict) -> list[Tag]:
        artist_profile = await ArtistDAO.find_one_or_none(artist_profile=user)

        if not artist_profile:
            raise NotFoundException("You don't have an artist profile")

        return await ArtistTagsDAO.find_all(user=user)
