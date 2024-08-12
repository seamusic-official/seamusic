from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.models.tags import Tag


@dataclass
class BaseTagsRepository(ABC):
    @abstractmethod
    async def add_tag(self, name: str) -> None:
        ...

    @abstractmethod
    async def get_my_listener_tags(self, user: dict) -> list[Tag]:
        ...

    @abstractmethod
    async def get_my_producer_tags(self, user: dict) -> list[Tag]:
        ...

    @abstractmethod
    async def get_my_artist_tags(self, user: dict) -> list[Tag]:
        ...
