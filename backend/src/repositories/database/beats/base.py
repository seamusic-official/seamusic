from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.models.beats import Beat


@dataclass
class BaseBeatsRepository(ABC):
    @abstractmethod
    async def get_user_beats(self, user_id: int) -> list[BeatDTO]:
        ...

    @abstractmethod
    async def all_beats(self) -> list[BeatDTO]:
        ...

    @abstractmethod
    async def get_one_beat(self, beat_id: int) -> BeatDTO:
        ...

    @abstractmethod
    async def update_beat(self, data: dict) -> None:
        ...

    @abstractmethod
    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        ...
