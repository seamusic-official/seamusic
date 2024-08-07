from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.schemas.beats import Beat


class SBeatCreate(Beat):
    pass


class SBeat(Beat):
    id: int
    username: str
    picture_url: str
    email: EmailStr


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

    model_config = ConfigDict(from_attributes=True)


class SCommentDeleteResponse(BaseModel):
    response: str = "Comment deleted"


class CommentCreate(BaseModel):
    """
    Это схема нужна для того что бы создать коментарию
    """

    comment: str


class CommentUpdate(BaseModel):
    comment: str


class CommentUpdateResponse(BaseModel):
    response: str = "Comment updated"


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

    model_config = ConfigDict(from_attributes=True)
