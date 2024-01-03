from music.services import MusicRepository
from music.schemas import SMusic
from fastapi import APIRouter, HTTPException


music = APIRouter(
    prefix = "/music",
    tags = ["Music & Albums"]
)

@music.get("/", summary="Create new music")
async def all():
    return await MusicRepository.find_all()

@music.post("/add", summary="Create new music")
async def create(music_data: SMusic):
    data = {
        "title": music_data.title,
        "description": music_data.description,
    }
    
    await MusicRepository.add_one(data)
    return data

@music.put("/update/{id}", summary="Create new music")
async def update(id: int, music_data: SMusic):
    data = {
        "title": music_data.title,
        "description": music_data.description,
    }
    
    await MusicRepository.edit_one(id, data)
    return data

@music.delete("/delete/{id}", summary="Create new music")
async def delete(id: int):
    return await MusicRepository.delete(id=id)

    
@music.post("/detail/{id}", summary="Create new music")
async def detail(id: int):
    return await MusicRepository.find_one_by_id(id=id)
    
    
