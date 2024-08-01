from abc import ABC

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from src.core.config import settings


class AbstractRepository(ABC):
    pass


class Spotify(AbstractRepository):
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=settings.spotify.CLIENT_ID,
            client_secret=settings.spotify.CLIENT_SECRET,
        )
    )

    @staticmethod
    def get_tracks():  # artist_id
        lz_uri = "spotify:artist:36QJpDe2go2KgaRleHCDTp"
        results = Spotify.sp.artist_top_tracks(lz_uri)
        tracks = []

        for track in results["tracks"]:
            track_data = {
                "id": track["id"],
                "type": "track",
                "name": track["name"],
                "preview_url": track["preview_url"],
                "image_url": track["album"]["images"][0]["url"],
                "spotify_url": track["external_urls"]["spotify"],
            }
            tracks.append(track_data)

        return tracks

    @staticmethod
    def get_tracks_from_album(album_id):
        results = Spotify.sp.album_tracks(album_id)
        tracks = []

        for track in results["items"]:
            track_data = {
                "id": track["id"],
                "type": "track",
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "preview_url": track["preview_url"],
                "spotify_url": track["external_urls"]["spotify"],
                "duration_ms": track["duration_ms"],
            }
            tracks.append(track_data)

        return tracks

    @staticmethod
    def track(track_id: int):
        results = Spotify.sp.track(track_id)
        return results["preview_url"]

    @staticmethod
    def get_albums():  # artist_id
        lz_uri = "spotify:artist:36QJpDe2go2KgaRleHCDTp"
        results = Spotify.sp.artist_albums(lz_uri)
        tracks = []

        for track in results["items"]:
            track_data = {
                "id": track["id"],
                "name": track["name"],
                "image_url": track["images"][0]["url"],
                "spotify_url": track["external_urls"]["spotify"],
            }
            tracks.append(track_data)

        return tracks

    @staticmethod
    def get_album(album_id):
        album = Spotify.sp.album(album_id)

        album_detail = {
            "id": album["id"],
            "name": album["name"],
            "image_url": album["images"][0]["url"],
            "spotify_url": album["external_urls"]["spotify"],
            "release_date": album["release_date"],
            "artists": album["artists"],
            "external_urls": album["external_urls"],
            "uri": album["uri"],
            "album_type": album["album_type"],
            "total_tracks": album["total_tracks"],
        }

        return album_detail

    @staticmethod
    def get_artist(artist_id: int):
        results = Spotify.sp.artist(artist_id)
        artists = []

        for artist in results["artist"]["items"]:
            track_data = {
                "name": artist["name"],
            }

            artists.append(track_data)

        return artists

    @staticmethod
    def search(query):
        results = Spotify.sp.search(q=query, type="track,artist,album")
        search_results = []

        # Поиск по артистам
        if "artists" in results and results["artists"]["items"]:
            artists = results["artists"]["items"]
            for artist in artists:
                data = {
                    "id": artist["id"],
                    "type": "artist",
                    "name": artist["name"],
                    "image_url": (
                        artist["images"][0]["url"] if artist.get("images") else None
                    ),
                    "popularity": artist["popularity"],
                }
                search_results.append(data)

        # Поиск по трекам
        if "tracks" in results and results["tracks"]["items"]:
            tracks = results["tracks"]["items"]
            for track in tracks:
                album = track["album"]
                data = {
                    "id": track["id"],
                    "type": "track",
                    "name": track["name"],
                    "artist": track["artists"][0]["name"],
                    "image_url": (
                        album["images"][0]["url"] if album.get("images") else None
                    ),
                    "album": album["name"],
                }
                search_results.append(data)

        # Поиск по альбомам
        if "albums" in results and results["albums"]["items"]:
            albums = results["albums"]["items"]
            for album in albums:
                data = {
                    "id": album["id"],
                    "type": "album",
                    "name": album["name"],
                    "artist": album["artists"][0]["name"],
                    "image_url": (
                        album["images"][0]["url"] if album.get("images") else None
                    ),
                    "release_date": album["release_date"],
                }
                search_results.append(data)

        return search_results
