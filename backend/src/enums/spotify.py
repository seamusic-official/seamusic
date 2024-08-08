from enum import Enum


class SpotifyAlbumType(str, Enum):
    album = "album"
    single = "single"
    compilation = "compilation"


class SpotifyTrackType(str, Enum):
    track = "track"
