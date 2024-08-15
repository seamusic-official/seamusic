from datetime import date

from dtos.database.base import BaseDTO, BaseResponseDTO


class SpotifyArtist(BaseDTO):
    external_urls: dict[str, str]
    href: str
    id: str
    name: str
    type: str
    uri: str


class Image(BaseDTO):
    url: str
    height: int
    width: int


class SpotifyAlbum(BaseDTO):
    album_type: str
    total_tracks: int
    available_markets: list[str]
    external_urls: dict[str, str]
    href: str
    id: str
    images: list[Image]
    name: str
    release_date: date
    release_date_precision: str
    restrictions: dict[str, str]
    type: str
    uri: str
    artists: list[SpotifyArtist]


class SpotifyTrack(BaseDTO):
    album: SpotifyAlbum
    artists: list[SpotifyArtist]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: dict[str, str]
    external_urls: dict[str, str]
    href: str
    id: str
    is_playable: bool
    linked_from: dict
    restrictions: dict[str, str]
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str
    is_local: bool


class SpotifyTrackResponseDTO(BaseResponseDTO):
    ...


class SpotifyTracksResponse(BaseResponseDTO):
    tracks: list[SpotifyTrack]


class SpotifyAlbumResponseDTO(BaseResponseDTO):
    ...


class SpotifyAlbumsResponseDTO(BaseResponseDTO):
    albums: list[SpotifyAlbum]
