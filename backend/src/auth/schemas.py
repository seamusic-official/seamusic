from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional, List
from src.tags.schemas import STag

class Role(str, Enum):
    superuser = "superuser"
    moder = "moder"
    artist = "artist"
    producer = "producer"
    listener = "listener"

"""
User (Listener) schemas
"""
class SUserBase(BaseModel):
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    picture_url: Optional[str]
    birthday: Optional[date]
    roles: List[Role]

class SUser(SUserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
class SUserUpdate(BaseModel):
    username: Optional[str] = Field(min_length=5, max_length=25)
    email: Optional[EmailStr]
    picture_url: Optional[str]
    tags: Optional[List[STag]]
    roles: Optional[List[Role]]

"""
Artist schemas
"""
class SArtistBase(BaseModel):
    user: SUser
    description: Optional[str]
    tags: Optional[List[STag]]

class SArtist(SArtistBase):
    id: int
    created_at: datetime
    updated_at: datetime

class SArtistUpdate(BaseModel):
    description: Optional[str] = Field(max_length=255)

"""
Producer schemas
"""
class SProducerBase(BaseModel):
    user: SUser
    description: Optional[str]
    tags: Optional[List[STag]]
    
class SProducer(SProducerBase):
    id: int
    created_at: datetime
    updated_at: datetime

class SProducerUpdate(BaseModel):
    description: Optional[str] = Field(max_length=255)

"""
Auth schemas
"""
class SRegisterUser(BaseModel):
    username: str = Field(min_length=3, max_length=25)
    password: str = Field(min_length=5)
    email: EmailStr
    roles: List[Role]
    birthday: Optional[date]
    tags: Optional[List[STag]]
    
class SLoginUser(BaseModel):
    email: EmailStr
    password: str
