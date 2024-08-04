from typing import List

from fastapi import APIRouter, status

from src.schemas.music import SSpotifyMusicResponse, SSpotifyAlbumResponse
from src.services.music import Spotify


music = APIRouter(prefix="/music", tags=["Inspiration"])


@music.get(
    path="/tracks",
    summary="Get music from spotify",
    response_model=List[SSpotifyMusicResponse],
    responses={status.HTTP_200_OK: {"model": List[SSpotifyMusicResponse]}},
)
async def get_spotify_tracks() -> List[SSpotifyMusicResponse]:
    return Spotify.get_tracks()


@music.get(path="/track/{music_id}", summary="Create new music")
async def get_spotify_track(music_id: int):
    return Spotify.track(music_id)


@music.get(
    path="/spotify/albums",
    summary="Get album from spotify",
    response_model=List[SSpotifyAlbumResponse],
    responses={status.HTTP_200_OK: {"model": List[SSpotifyAlbumResponse]}},
)
async def get_spotify_albums() -> List[SSpotifyAlbumResponse]:
    return Spotify.get_albums()


@music.get(path="/spotify/album", summary="Create new music")
async def get_spotify_album(album_id):
    return Spotify.get_album(album_id)


@music.get(path="/spotify/tracks_from_album", summary="Create new music")
async def get_tracks_from_album(album_id):
    return Spotify.get_tracks_from_album(album_id)


@music.get(path="/spotify/artist", summary="Create new music")
async def get_spotify_artist(artist_id):
    return Spotify.get_artist(artist_id)


@music.get(
    path="/spotify/search",
    summary="Search in spotify",
)
async def get_spotify_search(query):
    # ???
    return Spotify.search(query)