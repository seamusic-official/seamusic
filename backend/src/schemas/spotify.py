import datetime
from typing import List

from pydantic import BaseModel

from src.schemas.base import BaseResponse


class SpotifyTrack(BaseModel):
    id: str
    type: str
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SSpotifyTracksResponse(BaseResponse):
    tracks: List[SpotifyTrack]


class SSpotifyTrackResponse(BaseResponse):
    preview_url: str


class SpotifyAlbum(BaseModel):
    id: str
    name: str
    image_url: str
    spotify_url: str


class SSpotifyAlbumsResponse(BaseResponse):
    albums: List[SpotifyAlbum]


class Artist(BaseModel):
    id: int
    type: str
    name: str
    image_url: str
    popularity: 


class SSpotifyAlbumResponse(BaseResponse):
    id: int
    name: str
    image_url: str
    spotify_url: str
    release_date: datetime.date
    artists: List[Artist]
    external_urls: List[str]
    uri: str
    album_type:
    total_tracks:






















class SMusic(BaseModel):
    title: str
    description: str
    # author_id: int


# class SMusic(BaseModel):
#     id: str
#     title: str
#     description: str
#     picture: -
#     author_id: int
#     album_id: int


class SAlbum(BaseModel):
    id: str
    title: str
    description: str
    parental_advisory: bool
    author_id: int


class SpotifyMusic(BaseModel):
    id: str
    type: str
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SSpotifyMusicResponse(BaseResponse):
    # _model_type =
    ...





class SSpotifySearchResponse(BaseResponse):
    id: str
    type: str
    name: str
    image_url: str
    popularity: int
