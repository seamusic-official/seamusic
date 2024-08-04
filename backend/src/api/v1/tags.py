from typing import List

from fastapi import APIRouter, Depends

from src.core.exceptions import CustomException
from src.schemas.auth import SUser
from src.schemas.tags import STag
from src.services.auth import ProducerDAO, ArtistDAO
from src.services.tags import ListenerTagsDAO, ProducerTagsDAO, ArtistTagsDAO, TagsDAO
from src.utils.auth import get_current_user


tags = APIRouter(prefix="/tags", tags=["All tags"])


@tags.post("/", summary="Add tags")
async def add_tag(
    tag_data: STag, user: SUser = Depends(get_current_user)
) -> List[STag]:
    # ???
    listener_tags = await TagsDAO(tag_data)
    return listener_tags


@tags.get("/my_listener_tags", summary="Get my listener tags")
async def get_my_listener_tags(user: SUser = Depends(get_current_user)) -> List[STag]:
    # ???
    listener_tags = await ListenerTagsDAO(listener_profile=user)
    return listener_tags


@tags.get("/my_producer_tags", summary="Get my producer tags")
async def get_my_producer_tags(user: SUser = Depends(get_current_user)) -> List[STag]:
    # ???
    producer_profile = await ProducerDAO.find_one_or_none(producer_profile=user)
    if not producer_profile:
        raise CustomException(404, "You don't have a producer profile")

    producer_tags = await ProducerTagsDAO(producer_profile=producer_profile)
    return producer_tags


@tags.get("/my_artist_tags", summary="Get my artist tags")
async def get_my_artist_tags(user: SUser = Depends(get_current_user)) -> STag:
    # ???
    artist_profile = await ArtistDAO.find_one_or_none(artist_profile=user)
    if not artist_profile:
        raise CustomException(404, "You don't have a artist profile")

    artist_tags = await ArtistTagsDAO(user=user)
    return artist_tags