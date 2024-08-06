from typing import List

from pydantic import BaseModel

from src.schemas.base import BaseResponse


class Tag(BaseModel):
    name: str


class SAddTagRequest(BaseModel):
    name: str


class SAddTagResponse(BaseResponse):
    tags: List[Tag]


class SMyListenerTagsResponse(BaseResponse):
    tags: List[Tag]


class SMyProducerTagsResponse(BaseResponse):
    tags: List[Tag]


class SMyArtistTagsResponse(BaseResponse):
    tags: List[Tag]
