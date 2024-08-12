from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.repositories.dtos.beatpacks import BeatpackDTO


@dataclass
class BaseBeatpacksRepository(ABC):
    @abstractmethod
    async def get_user_beatpacks(self, user: dict) -> list[BeatpackDTO]:
        ...

    @abstractmethod
    async def get_all_beatpacks(self) -> list[BeatpackDTO]:
        ...

    @abstractmethod
    async def get_one_beatpack(self, beatpack_id: int) -> BeatpackDTO:
        ...

    @abstractmethod
    async def add_beatpack(self, data: dict) -> None:
        ...

    @abstractmethod
    async def update_beatpack(self, data: dict) -> None:
        ...

    @abstractmethod
    async def delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
        ...
