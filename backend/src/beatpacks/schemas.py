from pydantic import BaseModel
from typing import List, Optional

class BeatCreate(BaseModel):
    id: int

class BeatpackCreate(BaseModel):
    title: str
    description: str
    beats: List[BeatCreate]

class BeatResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class BeatpackResponse(BaseModel):
    id: int
    title: str
    description: str
    beats: List[BeatResponse]

    class Config:
        orm_mode = True
