from src.repositories.spotify import Spotify


class SpotifyService:
    @staticmethod
    async def get_spotify_tracks() -> list[dict]:
        return Spotify.get_tracks()

    @staticmethod
    async def get_spotify_track(music_id: int) -> dict:
        return Spotify.track(music_id)

    @staticmethod
    async def get_spotify_albums() -> list[dict]:
        return Spotify.get_albums()

    @staticmethod
    async def get_spotify_album(album_id: int) -> dict:
        return Spotify.get_album(album_id)

    @staticmethod
    async def get_tracks_from_album(album_id) -> list[dict]:
        return Spotify.get_tracks_from_album(album_id)

    @staticmethod
    async def get_spotify_artist(artist_id: int) -> dict:
        return Spotify.get_artist(artist_id)

    @staticmethod
    async def get_spotify_search(query: str) -> list[dict]:
        return Spotify.search(query)
