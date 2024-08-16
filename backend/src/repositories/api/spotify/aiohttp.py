from dataclasses import dataclass

import jmespath

from src.dtos.api.spotify import SearchResponseDTO
from src.dtos.database.albums import AlbumsResponseDTO, AlbumResponseDTO
from src.dtos.database.auth import ArtistResponseDTO
from src.dtos.database.tracks import TracksResponseDTO, TrackResponseDTO
from src.enums.spotify import SpotifyType
from src.repositories.api.base import AiohttpRepositpry
from src.repositories.api.spotify.base import BaseSpotifyRepository


@dataclass
class SpotifyRepository(BaseSpotifyRepository, AiohttpRepositpry):
    async def get_tracks(self, artist_id: int) -> TracksResponseDTO:
        async with self.session.get(f'{self.base_url}/artists/{artist_id}/top-tracks') as response:
            return TracksResponseDTO(**await response.json())

    async def get_album_tracks_count(self, album_id: int) -> int:
        async with self.session.get(f'{self.base_url}/albums/{album_id}/tracks') as response:
            data = await response.json()
            return jmespath.search('total', data)

    async def get_track(self, track_id: int) -> TrackResponseDTO | None:
        async with self.session.get(f'{self.base_url}/tracks/{track_id}') as response:
            return TrackResponseDTO(**await response.json()) if response.status != 404 else None

    async def get_albums(self, artist_id: int) -> AlbumsResponseDTO:
        async with self.session.get(f'{self.base_url}/artists/{artist_id}/albums') as response:
            return AlbumsResponseDTO(**await response.json()) if response.status != 404 else None

    async def get_album(self, album_id: int) -> AlbumResponseDTO | None:
        async with self.session.get(f'{self.base_url}/albums/{album_id}') as response:
            return AlbumResponseDTO(**await response.json()) if response.status != 404 else None

    async def get_artist(self, artist_id: int) -> ArtistResponseDTO | None:
        async with self.session.get(f'{self.base_url}/artists/{artist_id}') as response:
            return ArtistResponseDTO(**await response.json()) if response.status != 404 else None

    async def search(self, query: str, type_: SpotifyType) -> SearchResponseDTO:
        async with self.session.get(f'{self.base_url}/search?q={query}&type={type_}') as response:
            return SearchResponseDTO(**await response.json())
