from src.albums.services import AlbumsRepository
from src.albums.schemas import SAlbumBase, SAlbum, SAlbumCreate
from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user
from src.config import settings
from src.services import MediaRepository

from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse


albums = APIRouter(
    prefix = "/albums",
    tags = ["Albums"]
)

@albums.get("/my", summary="albums by current user")
async def get_user_albums(user: SUser = Depends(get_current_user)):
    response = await AlbumsRepository.find_all(user=user)
    return response

@albums.get("/all", summary="Get all albums")
async def all_albums():
    return await AlbumsRepository.find_all()

@albums.get("/get_one/{id}", summary="Get one album by id")
async def get_one_album(id: int):
    return await AlbumsRepository.find_one_by_id(id)

@albums.post("/add", summary="Init a album with file")
async def add_albums(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_album_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id,
        "type": "album"
    }

    response = await AlbumsRepository.add_one(data)
    return response

@albums.post("/picture/{albums_id}", summary="Update a picture for one album by id")
async def update_pic_albums(albums_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_album_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)

    data = {
        "picture_url": file_url
    }
    
    response = await AlbumsRepository.edit_one(albums_id, data)
    return response

@albums.post("/release/{id}", summary="Release one album by id")
async def release_albums(id: int, albums_data: SAlbumBase, user: SUser = Depends(get_current_user)):    
    data = {
        "title": albums_data.title ,
        "description": albums_data.description,
        "co_prod": albums_data.co_prod,
    }

    await AlbumsRepository.edit_one(id, data)
    return data

@albums.put("/update/{id}", summary="Create new albums")
async def update_albums(id: int, albums_data: SAlbumBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": albums_data.title,
        "description": albums_data.description,
        "prod_by": albums_data.prod_by
    }
    
    await AlbumsRepository.edit_one(id, data)
    return data

@albums.delete("/delete/{id}", summary="Create new albums")
async def delete_albums(id: int):
    return await AlbumsRepository.delete(id=id)

