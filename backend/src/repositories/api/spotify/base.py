from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.api.spotify import (
    SearchResponseDTO,
    SpotifyArtistResponseDTO,
    SpotifyAlbumResponseDTO,
    SpotifyAlbumsResponseDTO,
    SpotifyTrackResponseDTO,
    SpotifyTracksResponseDTO
)
from src.enums.spotify import SpotifyType


@dataclass
class BaseSpotifyRepository(ABC):
    base_url = 'https://api.spotify.com/v1'

    @abstractmethod
    async def login(self, code) -> str:
        ...

    @abstractmethod
    async def get_me(self, access_token: str) -> dict:
        ...

    @abstractmethod
    async def get_tracks(self, artist_id: int) -> SpotifyTracksResponseDTO:
        ...

    @abstractmethod
    async def get_album_tracks_count(self, album_id: int) -> int:
        ...

    @abstractmethod
    async def get_track(self, track_id: int) -> SpotifyTrackResponseDTO | None:
        ...

    @abstractmethod
    async def get_albums(self, artist_id: int) -> SpotifyAlbumsResponseDTO:
        ...

    @abstractmethod
    async def get_album(self, album_id: int) -> SpotifyAlbumResponseDTO | None:
        ...

    @abstractmethod
    async def get_artist(self, artist_id: int) -> SpotifyArtistResponseDTO | None:
        ...

    @abstractmethod
    async def search(self, query: str, type_: SpotifyType) -> SearchResponseDTO:
        ...
