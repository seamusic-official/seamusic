from src.dtos.database.tags import AddTagRequestDTO, TagsResponseDTO
from src.exceptions.services import NotFoundException
from src.models.tags import Tag
from src.repositories import Repositories, BaseMediaRepository
from src.repositories.database.tags.base import BaseTagsRepository


class TrackRepositories(Repositories):
    database: BaseTagsRepository
    media: BaseMediaRepository

class TagsService:
    repositories: TrackRepositories


    async def add_tag(self, name: str) -> None:
        tag = AddTagRequestDTO(name=name)

        return await self.repositories.database.add_tag(tag=tag)


    async def get_my_listener_tags(
        self,
        user_id: int
    ) -> list[TagsResponseDTO]:
        return await self.repositories.database.get_listener_tags(user_id=user_id)


    async def get_my_producer_tags(self, user_id: int) -> list[TagsResponseDTO]:
        producer_profile = await self.repositories.database.get_producer_tags(producer_id=user_id)

        if not producer_profile:
            raise NotFoundException("You don't have a producer profile")

        return producer_profile


    async def get_my_artist_tags(self, user_id: int) -> list[TagsResponseDTO]:
        artist_profile = await self.repositories.database.get_artist_tags(artist_id=user_id)

        if not artist_profile:
            raise NotFoundException("You don't have an artist profile")

        return artist_profile

