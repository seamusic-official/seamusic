from dataclasses import dataclass

from sqlalchemy import select

from src.models.auth import User
from src.models.tags import Tag
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.tags.base import BaseTagsRepository


@dataclass
class TagsRepository(SQLAlchemyRepository, BaseTagsRepository):
    async def add_tag(self, name: str) -> None:
        tag = Tag(name=name)
        self.session.add(tag)

    async def get_my_listener_tags(self, user: dict) -> list[Tag]:
        user = User(**user)
        query = select(Tag).filter(user in Tag.listener_profiles)
        return list(await self.session.scalars(query))

    async def get_my_producer_tags(self, user: dict) -> list[Tag]:
        user = User(**user)
        query = select(Tag).filter(user in Tag.producer_profiles)
        return list(await self.session.scalars(query))

    async def get_my_artist_tags(self, user: dict) -> list[Tag]:
        user = User(**user)
        query = select(Tag).filter(user in Tag.artist_profiles)
        return list(await self.session.scalars(query))
