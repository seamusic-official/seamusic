from spotipy import SpotifyClientCredentials, Spotify

from src.core.config import settings
from src.repositories.api.base import BaseAPIRepository
from src.repositories.api.spotify.base import BaseSpotifyRepository


class SpotifyRepository(BaseSpotifyRepository, BaseAPIRepository):
    client = Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=settings.spotify.CLIENT_ID,
            client_secret=settings.spotify.CLIENT_SECRET,
        )
    )

    def get_tracks(self, artist_id: int) -> list[dict]:
        lz_uri = "spotify:artist:36QJpDe2go2KgaRleHCDTp"
        results = BaseSpotifyRepository.client.artist_top_tracks(lz_uri)
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

    def get_tracks_from_album(self, album_id: int) -> list[dict]:
        results = BaseSpotifyRepository.client.album_tracks(album_id)
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

    def get_track(self, track_id):
        results = BaseSpotifyRepository.client.track(track_id)
        return results["preview_url"]

    def get_albums(self, artist_id: int) -> list[dict]:
        lz_uri = "spotify:artist:36QJpDe2go2KgaRleHCDTp"
        results = BaseSpotifyRepository.client.artist_albums(lz_uri)
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

    def get_album(self, album_id: int) -> dict:
        album = BaseSpotifyRepository.client.album(album_id)

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

    def get_artist(self, artist_id: int) -> dict:
        return BaseSpotifyRepository.client.artist(artist_id)

    def search(self, query: str) -> list[dict]:
        results = BaseSpotifyRepository.client.search(q=query, type="track,artist,album")
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
