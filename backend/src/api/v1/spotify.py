from fastapi import APIRouter, status, Depends

from src.enums.spotify import SpotifyType
from src.schemas.spotify import (
    SSpotifyTracksResponse,
    SpotifyTrack,
    SSpotifyTrackResponse,
    SSpotifyAlbumsResponse,
    SpotifyAlbum,
    SSpotifyAlbumResponse,
    SSpotifyAlbumTracksCountResponse,
    SSpotifyArtistResponse,
    SSpotifySearchResponse,
)
from src.services.spotify import SpotifyService, get_spotify_service


spotify = APIRouter(prefix="/inspiration", tags=["Music & Albums"])


@spotify.get(
    path="/tracks",
    summary="Get Spotify tracks by specified artist",
    response_model=SSpotifyTracksResponse,
    status_code=status.HTTP_200_OK,
)
async def get_spotify_artist_tracks(
    spotify_artist_id: str,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyTracksResponse:

    tracks = list(map(
        lambda track: SpotifyTrack(
            id=track.id,
            type=SpotifyType.track,
            name=track.name,
            preview_url=track.preview_url,
            image_url=track.image_url,
            spotify_url=track.href,
        ),
        await service.get_spotify_tracks(artist_id=spotify_artist_id)
    ))

    return SSpotifyTracksResponse(tracks=tracks)


@spotify.get(
    path="/tracks/{track_id}",
    summary="Get spotify track",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyTracksResponse,
)
async def get_spotify_track(
    track_id: str,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyTrackResponse:

    track = await service.get_spotify_track(track_id=track_id)

    return SSpotifyTrackResponse(
        id=track.id,
        type=track.type,
        name=track.name,
        preview_url=track.preview_url,
        image_url=track.image_url,
        spotify_url=track.href,
    )


@spotify.get(
    path="/albums",
    summary="Get Spotify albums by artist",
    response_model=SSpotifyAlbumsResponse,
    status_code=status.HTTP_200_OK,
)
async def get_spotify_albums(
    artist_id: str,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyAlbumsResponse:

    albums = list(map(
        lambda album: SpotifyAlbum(
            id=album.id,
            name=album.name,
            image_url=album.image_url,
            spotify_url=album.spotify_url,
        ),
        await service.get_spotify_albums(artist_id=artist_id)
    ))

    return SSpotifyAlbumsResponse(albums=albums)


@spotify.get(
    path="/album/{album_id}",
    summary="Get Spotify album by ID",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyAlbumResponse,
)
async def get_spotify_album(
    album_id: str,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyAlbumResponse:

    album = await service.get_spotify_album(album_id=album_id)

    return SSpotifyAlbumResponse(
        id=album.id,
        name=album.name,
        image_url=album.image_url,
        spotify_url=album.spotify_url,
        release_date=album.release_date,
        artists=album.artists,
        external_urls=album.external_urls,
        uri=album.uri,
        album_type=album.album_type,
        total_tracks=album.total_tracks,
    )


@spotify.get(
    path="/album/{album_id}/tracks",
    summary="Get amount of tracks in album",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyAlbumTracksCountResponse,
)
async def get_album_tracks_count(
    album_id: str,
    service: SpotifyService = Depends(get_spotify_service)
) -> SSpotifyAlbumTracksCountResponse:

    return SSpotifyAlbumTracksCountResponse(count=await service.get_album_tracks_count(album_id=album_id))


@spotify.get(
    path="/artist/{artist_id}",
    summary="Get Spotify artist by ID",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyArtistResponse,
)
async def get_spotify_artist(
    artist_id: str,
    service: SpotifyService = Depends(get_spotify_service)
) -> SSpotifyArtistResponse:

    artist = await service.get_spotify_artist(artist_id=artist_id)

    return SSpotifyArtistResponse(
        id=artist.id,
        external_urls=artist.external_urls,
        type=artist.type,
        name=artist.name,
        image_url=artist.image_url,
        popularity=artist.popularity,
    )


@spotify.get(
    path="/spotify/search",
    summary="Search in spotify",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifySearchResponse,
)
async def search(
    query: str,
    type_: SpotifyType,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifySearchResponse:

    result = await service.get_spotify_search(query=query, type_=type_)

    return SSpotifySearchResponse(
        tracks=result.tracks,
        artists=result.artists,
        albums=result.albums,
    )
