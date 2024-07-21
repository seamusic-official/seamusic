from src.music.services import Spotify
from fastapi import APIRouter


music = APIRouter(
    prefix = "/music",
    tags = ["Music & Albums"]
)


@music.get("/tracks", summary="Create new music")
async def get_spotify_tracks():
    return Spotify.get_tracks()

@music.get("/track/{id}", summary="Create new music")
async def get_spotify_track(id):
    return Spotify.track(id)

@music.get("/spotify/albums", summary="Create new music")
async def get_spotify_albums():
    return Spotify.get_albums()

@music.get("/spotify/album", summary="Create new music")
async def get_spotify_album(album_id):
    return Spotify.get_album(album_id)

@music.get("/spotify/tracks_from_album", summary="Create new music")
async def get_tracks_from_album(album_id):
    return Spotify.get_tracks_from_album(album_id)

@music.get("/spotify/artist", summary="Create new music")
async def get_spotify_artist(artist_id):
    return Spotify.get_artist(artist_id)

@music.get("/spotify/search", summary="Create new music")
async def get_spotify_search(query):
    return Spotify.search(query)
