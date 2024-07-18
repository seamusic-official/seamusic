from pydantic import BaseModel, Field
# from src.auth.schemas import SUser
from pydantic import BaseModel, EmailStr
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



class CommentCreate(BaseModel):
    
    """

    Это схема нужно для того что бы создать коментарию

    """

    comment: str


class CommentUpdate(BaseModel):
    comment: str
    

class GetAuthor(BaseModel):
    id: int
    username: str
    picture_url: str
    email: EmailStr


class CommentResponse(BaseModel):
    id: int
    comment: str
    comment_creator_id: int
    beat_id: Optional[int] = None
    beat_pack_id: Optional[int] = None
    soundkit_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    is_available: bool
    comment_author: GetAuthor

    class Config:
        orm_mode = True

