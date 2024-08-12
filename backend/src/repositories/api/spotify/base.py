from abc import ABC, abstractmethod
from dataclasses import dataclass

from spotipy import Spotify


@dataclass
class BaseSpotifyRepository(ABC):
    client: Spotify

    @abstractmethod
    def get_tracks(self, artist_id: int) -> list[dict]:
        ...

    @abstractmethod
    def get_tracks_from_album(self, album_id: int) -> list[dict]:
        ...

    @abstractmethod
    def get_track(self, track_id: int) -> str:
        ...

    @abstractmethod
    def get_albums(self, artist_id: int) -> list:
        ...

    @abstractmethod
    def get_album(self, album_id: int) -> dict:
        ...

    @abstractmethod
    def get_artist(self, artist_id: int) -> dict:
        ...

    @abstractmethod
    def search(self, query: str) -> list[dict]:
        ...
