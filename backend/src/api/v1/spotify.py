from typing import List

from fastapi import APIRouter, status

from src.schemas.spotify import (
    SSpotifyTracksResponse,
    SSpotifyAlbumResponse,
    SSpotifyTrackResponse,
    SSpotifyAlbumsResponse,
    SSpotifyAlbumTracksResponse,
    SSpotifyArtistResponse,
    SSpotifySearchResponse
)
from src.services.spotify import Spotify


music = APIRouter(prefix="/music", tags=["Spotify"])


@music.get(
    path="/tracks",
    summary="Get music from spotify",
    response_model=List[SSpotifyTracksResponse],
    responses={status.HTTP_200_OK: {"model": List[SSpotifyTracksResponse]}},
)
async def get_spotify_tracks() -> SSpotifyTracksResponse:
    return Spotify.get_tracks()


@music.get(
    path="/track/{music_id}",
    summary="Create new music",
    response_model=SSpotifyTrackResponse,
    responses={status.HTTP_200_OK: {"model": SSpotifyTrackResponse}}
)
async def get_spotify_track(music_id: int) -> SSpotifyTrackResponse:
    return Spotify.track(music_id)


@music.get(
    path="/spotify/albums",
    summary="Get albums from spotify",
    response_model=SSpotifyAlbumsResponse,
    responses={status.HTTP_200_OK: {"model": SSpotifyAlbumsResponse}},
)
async def get_spotify_albums() -> SSpotifyAlbumsResponse:
    return Spotify.get_albums()


@music.get(
    path="/spotify/album",
    summary="Get an album from spotify",
    response_model=SSpotifyAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SSpotifyAlbumResponse}}
)
async def get_spotify_album(album_id: int) -> SSpotifyAlbumResponse:
    return Spotify.get_album(album_id)


@music.get(
    path="/spotify/tracks_from_album",
    summary="Create new music",
    response_model=SSpotifyAlbumTracksResponse,
    responses={status.HTTP_200_OK: {"model": SSpotifyAlbumTracksResponse}}
)
async def get_tracks_from_album(album_id) -> SSpotifyAlbumTracksResponse:
    return Spotify.get_tracks_from_album(album_id)


@music.get(
    path="/spotify/artist",
    summary="Create new music",
    response_model=SSpotifyArtistResponse,
    responses={status.HTTP_200_OK: {"model": SSpotifyArtistResponse}}
)
async def get_spotify_artist(artist_id) -> SSpotifyArtistResponse:
    return Spotify.get_artist(artist_id)


@music.get(
    path="/spotify/search",
    summary="Search in spotify",
    response_model=SSpotifySearchResponse,
    responses={status.HTTP_200_OK: {"model": SSpotifySearchResponse}}
)
async def get_spotify_search(query: str) -> SSpotifySearchResponse:
    return Spotify.search(query)
