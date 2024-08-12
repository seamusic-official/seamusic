from pydantic import BaseModel

from src.models.auth import User
from src.models.beats import Beat


class BeatpackDTO(BaseModel):
    title: str
    description: str
    users: list[User]
    beats: list[Beat]