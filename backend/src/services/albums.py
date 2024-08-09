from io import BytesIO

from src.core.media import MediaRepository
from src.exceptions.services import NoRightsException
from src.models.albums import Album
from src.repositories.albums import AlbumsRepository


class AlbumService:
    @staticmethod
    async def get_user_albums(user_id: int) -> list[Album]:
        return await AlbumsRepository.find_all(user_id=user_id)

    @staticmethod
    async def get_all_albums() -> list[Album]:
        return await AlbumsRepository.find_all()

    @staticmethod
    async def get_one_album(album_id: int) -> Album:
        return await AlbumsRepository.find_one_by_id(album_id)

    @staticmethod
    async def add_album(
        file_stream: BytesIO,
        file_info: str | None,
        prod_by: str,
        user_id: int,
    ) -> Album:
    
        file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file_stream)
        data = {
            "title": "Unknown title",
            "file_url": file_url,
            "prod_by": prod_by,
            "user_id": user_id,
            "type": "album",
        }
    
        return await AlbumsRepository.add_one(data)

    @staticmethod
    async def update_album_picture(
        album_id: int,
        file_info: str | None,
        file_stream: BytesIO,
        user_id: int
    ) -> Album:
    
        album = await AlbumsRepository.find_one_by_id(id_=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()
    
        file_url = await MediaRepository.upload_file("PICTURES", file_info, file_stream)
        data = {"picture_url": file_url}
    
        return await AlbumsRepository.edit_one(album_id, data)

    @staticmethod
    async def release_album(
        album_id: int,
        name: str,
        description: str,
        co_prod: str,
        user_id: int,
    ) -> Album:
    
        album = await AlbumsRepository.find_one_by_id(id_=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()
    
        data = {
            "name": name,
            "description": description,
            "co_prod": co_prod,
        }
    
        return await AlbumsRepository.edit_one(album_id, data)

    @staticmethod
    async def update_album(
        user_id: int,
        album_id: int,
        title: str,
        description: str,
        prod_by: str,
    ) -> Album:
    
        album = await AlbumsRepository.find_one_by_id(id_=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()
    
        data = {
            "name": title,
            "description": description,
            "prod_by": prod_by,
        }
    
        return await AlbumsRepository.edit_one(album_id, data)

    @staticmethod
    async def delete_albums(album_id: int, user_id: int) -> None:
    
        album = await AlbumsRepository.find_one_by_id(id_=album_id)
    
        if album.user.id != user_id:
            raise NoRightsException()
    
        await AlbumsRepository.delete(id_=album_id)
