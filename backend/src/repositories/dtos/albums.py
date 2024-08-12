from pydantic import BaseModel


class AlbumDTO(BaseModel):
    name: str
    picture_url: str
    description: str
    co_prod: str

    type: str
    user_id: int
