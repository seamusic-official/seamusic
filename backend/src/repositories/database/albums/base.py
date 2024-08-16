from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.albums import CreateAlbumRequestDTO, AlbumResponseDTO, AlbumsResponseDTO


@dataclass
class BaseAlbumRepository(ABC):

    @abstractmethod
    async def get_album_by_id(self, album_id: int) -> AlbumResponseDTO:
        ...

    @abstractmethod
    async def get_all_albums(self) -> AlbumsResponseDTO:
        ...

    @abstractmethod
    async def get_user_albums(self, user_id: int) -> AlbumsResponseDTO:
        ...

    @abstractmethod
    async def create_album(self, album: CreateAlbumRequestDTO) -> None:
        ...

    @abstractmethod
    async def edit_album(self, album: CreateAlbumRequestDTO) -> None:
        ...

    @abstractmethod
    async def delete_album(self, album_id: int, user_id: int) -> None:
        ...
