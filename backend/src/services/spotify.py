from dataclasses import dataclass

from src.repositories.api.spotify.base import BaseSpotifyRepository


@dataclass
class SpotifyService():
    @staticmethod
    async def get_spotify_tracks() -> list[dict]:
        return BaseSpotifyRepository.get_tracks()

    @staticmethod
    async def get_spotify_track(music_id: int) -> dict:
        return BaseSpotifyRepository.get_track(music_id)

    @staticmethod
    async def get_spotify_albums() -> list[dict]:
        return BaseSpotifyRepository.get_albums()

    @staticmethod
    async def get_spotify_album(album_id: int) -> dict:
        return BaseSpotifyRepository.get_album(album_id)

    @staticmethod
    async def get_tracks_from_album(album_id) -> list[dict]:
        return BaseSpotifyRepository.get_album_tracks_count(album_id)

    @staticmethod
    async def get_spotify_artist(artist_id: int) -> dict:
        return BaseSpotifyRepository.get_artist(artist_id)

    @staticmethod
    async def get_spotify_search(query: str) -> list[dict]:
        return BaseSpotifyRepository.search(query)
