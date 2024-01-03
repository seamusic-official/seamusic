from pydantic import BaseModel


class SMusic(BaseModel):
    title: str
    description: str
    #author_id: int

"""
class SMusic(BaseModel):
    id: str
    title: str
    description: str
    picture: -
    author_id: int
    album_id: int
"""

class SAlbum(BaseModel):
    id: str
    title: str
    description: str
    parental_advisory: bool
    author_id: int