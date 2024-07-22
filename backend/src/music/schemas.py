from pydantic import BaseModel


class SMusic(BaseModel):
    title: str
    description: str
    #author_id: int

"""
class SMusic(BaseModel):
    id: str
    title: str
    description: str
    picture: -
    author_id: int
    album_id: int
"""

class SAlbum(BaseModel):
    id: str
    title: str
    description: str
    parental_advisory: bool
    author_id: int


class SSpotifyMusicResponse(BaseModel):
    id: str
    type: str
    name: str
    preview_url: str
    image_url: str
    spotify_url: str

class SSpotifyAlbumResponse(BaseModel):
    id: str
    name: str
    image_url: str
    spotify_url: str

class SSpotifySearchResponse(BaseModel):
    id: str
    type: str
    name: str
    image_url: str
    popularity: int