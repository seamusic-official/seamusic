from src.tracks.services import TracksRepository
from src.tracks.schemas import STrackBase, STrack, STrackCreate
from src.auth.schemas import SUser
from src.tracks.utils import save_audio, save_image
from src.config import settings
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse

tracks = APIRouter(
    prefix = "/tracks",
    tags = ["Tracks"]
)

@tracks.get("/my", summary="tracks by current user")
async def get_user_tracks(user: SUser = Depends(get_current_user)):
    response = await TracksRepository.find_all(user=user)
    return response

@tracks.get("/all", summary="Get all tracks")
async def all_tracks():
    return await TracksRepository.find_all()

@tracks.get("/get_one/{id}", summary="Get one beat by id")
async def get_one_beat(id: int):
    return await TracksRepository.find_one_by_id(id)

@tracks.post("/add", summary="Init a beat with file")
async def add_tracks(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("AUDIOFILES", file_info, file)
    
    data = {
        "title": "Unknown title",
        "file_url": file_url,
        "prod_by": user.username,
        "user_id": user.id
    }

    response = await TracksRepository.add_one(data)
    return response

@tracks.post("/picture/{tracks_id}", summary="Update a picture for one beat by id")
async def update_pic_tracks(tracks_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await unique_filename(file) if file else None
    file_url = await MediaRepository.upload_file("PICTURES", file_info, file)

    data = {
        "picture_url": file_url
    }
    
    response = await TracksRepository.edit_one(tracks_id, data)
    return response

@tracks.post("/release/{id}", summary="Release one beat by id")
async def release_tracks(id: int, tracks_data: SBeatBase, user: SUser = Depends(get_current_user)):    
    data = {
        "title": tracks_data.title ,
        "description": tracks_data.description,
        "co_prod": tracks_data.co_prod,
    }

    await TracksRepository.edit_one(id, data)
    return data

@tracks.put("/update/{id}", summary="Create new tracks")
async def update_tracks(id: int, tracks_data: SBeatBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": tracks_data.title,
        "description": tracks_data.description,
        "prod_by": tracks_data.prod_by
    }
    
    await TracksRepository.edit_one(id, data)
    return data

@tracks.delete("/delete/{id}", summary="Create new tracks")
async def delete_tracks(id: int):
    return await TracksRepository.delete(id=id)

