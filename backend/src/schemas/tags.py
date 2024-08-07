from typing import List

from pydantic import BaseModel


class Tag(BaseModel):
    name: str


class SAddTagRequest(BaseModel):
    name: str


class SAddTagResponse(BaseModel):
    tags: List[Tag]


class SMyListenerTagsResponse(BaseModel):
    tags: List[Tag]


class SMyProducerTagsResponse(BaseModel):
    tags: List[Tag]


class SMyArtistTagsResponse(BaseModel):
    tags: List[Tag]
