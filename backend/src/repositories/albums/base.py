from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from src.models.albums import Album


@dataclass
class BaseAlbumRepository(ABC):

    @abstractmethod
    async def create_album(self, album: Album) -> None:
        ...

    @abstractmethod
    async def get_album_by_id(self, album_id: int) -> Album:
        ...

    @abstractmethod
    async def edit_album(self, album: Album) -> Album:
        ...

    @abstractmethod
    async def get_all_albums(self) -> Iterable[Album]:
        ...

    @abstractmethod
    async def get_all_user_albums(self, user_id: int) -> Iterable[Album]:
        ...

    @abstractmethod
    async def delete_album(self, album_id: int,user_id: int) -> None:
        ...
