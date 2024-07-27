from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class SCommentDeleteResponse(BaseModel):
    response: str = 'Comment deleted'


class CommentCreate(BaseModel):
    """
    Это схема нужно для того что бы создать коментарию
    """
    comment: str


class CommentUpdate(BaseModel):
    comment: str
    
class CommentUpdateResponse(BaseModel):
    response: str = 'Comment updated'


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

