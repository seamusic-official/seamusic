from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

class Role(str, Enum):
    Artist = "Artist"
    Producer = "Producer"
    Listener = "Listener"

class SUser(BaseModel):
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    birthday: Optional[date]
    role: Role
    registered_at: date
    
    
class SRegisterUser(BaseModel):
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    birthday: Optional[date]
    password: str
    role: Role
    
class SLoginUser(BaseModel):
    email: EmailStr
    password: str

class SArtist(BaseModel):
    user_id: int
    user: SUser
    description: str

class SProducer(BaseModel):
    user_id: int
    user: SUser
    description: str
    
class SListener(BaseModel):
    user_id: int
    user: SUser
    description: str
