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
    birthday: Optional[date]
    role: Role
    
class SUser(SUserBase):
    id: int
    created_at: datetime
    updated_at: datetime

class SArtistBase(BaseModel):
    user_id: int
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