import asyncio
from src.music.services import Spotify
from src.music.utils import get_wikipedia_summary_async
from fastapi import APIRouter, HTTPException
from fastapi_cache.decorator import cache


music = APIRouter(
    prefix = "/music",
    tags = ["Music & Albums"]
)

@music.get("/wikipedia/summary/{query}")
async def get_wikipedia_summary(query: str):
    summary = await get_wikipedia_summary_async(query)
    return {"summary": summary}

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
