from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.models.soundkits import Soundkit


@dataclass
class BaseSoundkitsRepository(ABC):
    @abstractmethod
    async def get_user_soundkits(self, user_id: int) -> list[Soundkit]:
        ...

    @abstractmethod
    async def get_all_soundkits(self) -> list[Soundkit]:
        ...

    @abstractmethod
    async def get_license_by_id(self, soundkit_id: int) -> Soundkit | None:
        ...

    @abstractmethod
    async def add_soundkit(self, soundkit: Soundkit) -> None:
        ...

    @abstractmethod
    async def update_license(self, soundkit: Soundkit) -> None:
        ...

    @abstractmethod
    async def delete_license(self, soundkit_id: int, user_id: int) -> None:
        ...
