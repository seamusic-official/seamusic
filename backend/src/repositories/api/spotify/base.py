from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.api.spotify import SearchResponseDTO
from src.dtos.database.albums import AlbumsResponseDTO, AlbumResponseDTO
from src.dtos.database.auth import ArtistResponseDTO
from src.dtos.database.tracks import TracksResponseDTO, TrackResponseDTO
from src.enums.spotify import SpotifyType


@dataclass
class BaseSpotifyRepository(ABC):
    base_url = 'https://api.spotify.com/v1'

    @abstractmethod
    async def get_tracks(self, artist_id: int) -> TracksResponseDTO:
        ...

    @abstractmethod
    async def get_album_tracks_count(self, album_id: int) -> int:
        ...

    @abstractmethod
    async def get_track(self, track_id: int) -> TrackResponseDTO | None:
        ...

    @abstractmethod
    async def get_albums(self, artist_id: int) -> AlbumsResponseDTO:
        ...

    @abstractmethod
    async def get_album(self, album_id: int) -> AlbumResponseDTO | None:
        ...

    async def get_artist(self, artist_id: int) -> ArtistResponseDTO | None:
        ...

    @abstractmethod
    async def search(self, query: str, type_: SpotifyType) -> SearchResponseDTO:
        ...
