from pydantic import BaseModel


class BeatDTO(BaseModel):
    title: str
    description: str
    picture_url: str
    file_url: str
    co_prod: str
    type: str
    user_id: int
