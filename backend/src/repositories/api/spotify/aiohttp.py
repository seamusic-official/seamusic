from dataclasses import dataclass

import jmespath

from src.core.config import settings
from src.dtos.api.spotify import (
    SearchResponseDTO,
    SpotifyArtistResponseDTO,
    SpotifyAlbumResponseDTO,
    SpotifyAlbumsResponseDTO,
    SpotifyTrackResponseDTO,
    SpotifyTracksResponseDTO
)
from src.enums.spotify import SpotifyType
from src.repositories.api.base import AiohttpRepositpry
from src.repositories.api.spotify.base import BaseSpotifyRepository


@dataclass
class SpotifyRepository(BaseSpotifyRepository, AiohttpRepositpry):
    async def login(self, code) -> str:
        payload = {
            "code": code,
            "client_id": settings.spotify.CLIENT_ID,
            "client_secret": settings.spotify.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": "http://localhost:5173/profile",
        }

        response = await self.session.post(
            url="https://accounts.spotify.com/api/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=payload,
        )
        data = await response.json()
        return jmespath.search('access_token', data)

    async def get_me(self, access_token: str) -> dict:
        response = await self.session.get(
            url="https://api.spotify.com/v1/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        return await response.json()

    async def get_tracks(self, artist_id: int) -> SpotifyTracksResponseDTO:
        async with self.session.get(f'{self.base_url}/artists/{artist_id}/top-tracks') as response:
            return SpotifyTracksResponseDTO(**await response.json())

    async def get_album_tracks_count(self, album_id: int) -> int:
        async with self.session.get(f'{self.base_url}/albums/{album_id}/tracks') as response:
            data = await response.json()
            return jmespath.search('total', data)

    async def get_track(self, track_id: int) -> SpotifyTrackResponseDTO | None:
        async with self.session.get(f'{self.base_url}/tracks/{track_id}') as response:
            return SpotifyTrackResponseDTO(**await response.json()) if response.status != 404 else None

    async def get_albums(self, artist_id: int) -> SpotifyAlbumsResponseDTO:
        async with self.session.get(f'{self.base_url}/artists/{artist_id}/albums') as response:
            return SpotifyAlbumsResponseDTO(**await response.json()) if response.status != 404 else None

    async def get_album(self, album_id: int) -> SpotifyAlbumResponseDTO | None:
        async with self.session.get(f'{self.base_url}/albums/{album_id}') as response:
            return SpotifyAlbumResponseDTO(**await response.json()) if response.status != 404 else None

    async def get_artist(self, artist_id: int) -> SpotifyArtistResponseDTO | None:
        async with self.session.get(f'{self.base_url}/artists/{artist_id}') as response:
            return SpotifyArtistResponseDTO(**await response.json()) if response.status != 404 else None

    async def search(self, query: str, type_: SpotifyType) -> SearchResponseDTO:
        async with self.session.get(f'{self.base_url}/search?q={query}&type={type_}') as response:
            return SearchResponseDTO(**await response.json())
