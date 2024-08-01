from fastapi import APIRouter

from src.services.music import Spotify


music = APIRouter(prefix="/music", tags=["Music & Albums"])


@music.get(path="/tracks", summary="Create new music")
async def get_spotify_tracks():
    return Spotify.get_tracks()


@music.get(path="/track/{track_id}", summary="Create new music")
async def get_spotify_track(track_id: int):
    return Spotify.track(track_id)


@music.get(path="/spotify/albums", summary="Create new music")
async def get_spotify_albums():
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


@music.get(path="/spotify/search", summary="Create new music")
async def get_spotify_search(query):
    return Spotify.search(query)
