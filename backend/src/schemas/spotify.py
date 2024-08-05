import datetime
from typing import List, Dict, Union

from pydantic import BaseModel

from src.enums.spotify import SpotifyAlbumType, SpotifyTrackType


class SpotifyTrack(BaseModel):
    id: str
    type: SpotifyTrackType
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SSpotifyTracksResponse(BaseModel):
    tracks: List[SpotifyTrack]


class SSpotifyTrackResponse(BaseModel):
    preview_url: str


class SpotifyAlbum(BaseModel):
    id: str
    name: str
    image_url: str
    spotify_url: str


class SSpotifyAlbumsResponse(BaseModel):
    albums: List[SpotifyAlbum]


class SpotifyArtist(BaseModel):
    id: int
    type: str
    name: str
    image_url: str
    popularity: int


class SSpotifyAlbumResponse(BaseModel):
    id: int
    name: str
    image_url: str
    spotify_url: str
    release_date: datetime.date
    artists: List[SpotifyArtist]
    external_urls: Dict[str, str]
    uri: str
    album_type: SpotifyAlbumType
    total_tracks: int


class SpotifyAlbumTrack(BaseModel):
    id: int
    type: SpotifyTrackType
    name: str
    artists: List[SpotifyArtist]
    preview_url: str
    spotify_url: str
    duration_ms: int


class SSpotifyAlbumTracksResponse(BaseModel):
    tracks: List[SpotifyAlbumTrack]


class SSpotifyArtistResponse(BaseModel):
    name: str


class SSpotifySearchResponse(BaseModel):
    results: List[Union[SpotifyArtist, SpotifyTrack, SpotifyAlbum]]
