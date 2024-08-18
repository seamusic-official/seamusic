from dataclasses import dataclass

from src.enums.spotify import SpotifyType
from src.repositories import Repositories
from src.repositories.api.spotify.base import BaseSpotifyRepository


class SpotifyRepositories(Repositories):
    api: BaseSpotifyRepository

@dataclass
class SpotifyService:
    repositories: SpotifyRepositories

    async def get_spotify_tracks(self, artist_id: int) -> list[dict]:
        return await self.repositories.api.get_tracks(artist_id=artist_id)


    async def get_spotify_track(self, track_id: int) -> str:
        return await self.repositories.api.get_track(track_id=track_id)


    async def get_spotify_albums(self, artist_id: int) -> list[dict]:
        return await self.repositories.api.get_albums(artist_id=artist_id)


    async def get_spotify_album(self, album_id: int) -> dict:
        return await self.repositories.api.get_album(album_id=album_id)


    async def get_tracks_from_album(self, album_id) -> list[dict]:
        return await self.repositories.api.get_album_tracks_count(album_id=album_id)


    async def get_spotify_artist(self, artist_id: int) -> dict:
        return await self.repositories.api.get_artist(artist_id=artist_id)


    async def get_spotify_search(self, query: str, type_: SpotifyType) -> list[dict]:
        return await self.repositories.api.search(query=query, type_=type_)
