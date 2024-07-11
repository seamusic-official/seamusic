from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional

class Role(str, Enum):
    Artist = "Artist"
    Producer = "Producer"
    Listener = "Listener"

class SUserBase(BaseModel):
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    picture_url: Optional[str]
    birthday: Optional[date]
    role: Role

class SUser(SUserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
class SUserUpdate(BaseModel):
    username: Optional[str] = Field(min_length=5, max_length=25)
    email: Optional[EmailStr]
    picture_url: Optional[str]

class SArtistBase(BaseModel):
    user: SUser
    description: Optional[str]

class SArtist(SArtistBase):
    id: int
    created_at: datetime
    updated_at: datetime

class SProducerBase(BaseModel):
    user_id: int
    user: SUser
    description: Optional[str]
    
class SProducer(SProducerBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SRegisterUser(BaseModel):
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    birthday: Optional[date]
    password: str
    role: Role
    
class SLoginUser(BaseModel):
    email: EmailStr
    password: str


class SUserResponse(BaseModel):
    id: int