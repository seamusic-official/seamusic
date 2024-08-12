from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.models.tracks import Track


@dataclass
class BaseTracksRepository(ABC):
    @abstractmethod
    async def get_my_tracks(self, user: dict) -> list[Track]:
        ...

    @abstractmethod
    async def all_tracks(self) -> list[Track]:
        ...

    @abstractmethod
    async def get_one_track(self, track_id: int) -> Track | None:
        ...

    @abstractmethod
    async def update_track(self, data: dict) -> None:
        ...

    @abstractmethod
    async def delete_track(self, track_id: int, user_id: int) -> None:
        ...
