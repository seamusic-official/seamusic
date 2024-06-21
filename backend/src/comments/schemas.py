from pydantic import BaseModel, Field
from src.auth.schemas import SUser
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SBeatBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    beat_pack_id: Optional[int]

class SBeatCreate(SBeatBase):
    pass

class SBeat(SBeatBase):
    id: int
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True

class SBeatPackBase(BaseModel):
    title: str
    description: str
    owner_id: int
    beats: List[SBeat] = Field(...)
    
class SBeatPackCreate(SBeatPackBase):
    pass

class SBeatPack(SBeatPackBase):
    id: int
    liked: bool
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True



class CommentResponse(BaseModel):

    id: int
    author: Optional[str] = None
    author_id: int
    comment: str
    date_pub: datetime
    