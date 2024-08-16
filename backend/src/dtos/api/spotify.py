from datetime import date

from dtos.database.base import BaseDTO, BaseResponseDTO


class SpotifyImage(BaseDTO):
    url: str
    height: int
    width: int


class SpotifyArtist(BaseDTO):
    external_urls: dict[str, str]
    images: list[SpotifyImage]
    genres: list[str]
    href: str
    id: str
    name: str
    type: str
    uri: str


class SpotifyAlbumTrack(BaseDTO):
    href: str
    next: str
    previous: str
    popularity: int
    items: list['SpotifyTrack']
    total: int


class SpotifyAlbum(BaseDTO):
    external_urls: dict[str, str]
    album_type: str
    total_tracks: int
    genres: list[str]
    href: str
    id: str
    images: list[SpotifyImage]
    tracks: list[SpotifyAlbumTrack]
    artists: list[SpotifyArtist]
    name: str
    release_date: date
    type: str
    uri: str


class SpotifyTrack(BaseDTO):
    external_urls: dict[str, str]
    external_ids: dict[str, str]
    album: SpotifyAlbum
    artists: list[SpotifyArtist]
    duration_ms: int
    explicit: bool
    href: str
    id: str
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str


class SpotifyTrackResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    external_ids: dict[str, str]
    album: SpotifyAlbum
    artists: list[SpotifyArtist]
    duration_ms: int
    explicit: bool
    href: str
    id: str
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str


class SpotifyTracksResponse(BaseResponseDTO):
    tracks: list[SpotifyTrack]


class SpotifyAlbumResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    album_type: str
    total_tracks: int
    genres: list[str]
    href: str
    id: str
    images: list[SpotifyImage]
    tracks: list[SpotifyAlbumTrack]
    artists: list[SpotifyArtist]
    name: str
    release_date: date
    type: str
    uri: str


class SpotifyAlbumsResponseDTO(BaseResponseDTO):
    albums: list[SpotifyAlbum]
