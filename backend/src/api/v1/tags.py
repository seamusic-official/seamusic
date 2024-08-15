from fastapi import APIRouter, Depends, status

from src.exceptions.api import NotFoundException, UnauthorizedException
from src.schemas.auth import User
from src.repositories.dtos.tags import (
    SAddTagRequest,
    SMyListenerTagsResponse,
    SMyProducerTagsResponse,
    SMyArtistTagsResponse,
    SAddTagResponse,
)
from src.repositories.database.auth import ProducerDAO, ArtistDAO
from src.repositories.tags import ListenerTagsDAO, ProducerTagsDAO, ArtistTagsDAO, TagsDAO
from src.utils.auth import get_current_user

tags = APIRouter(prefix="/tags", tags=["All tags"])


@tags.post(
    path="/",
    summary="Add tags",
    response_model=SAddTagResponse,
    responses={status.HTTP_200_OK: {"model": SAddTagResponse}},
)
async def add_tag(
    tag: SAddTagRequest, user: User = Depends(get_current_user)
) -> SAddTagResponse:

    if user:
        listener_tags = await TagsDAO.add_one(tag.model_dump())
        return SAddTagResponse(tags=listener_tags)
    raise UnauthorizedException()


@tags.get(
    path="/my_listener_tags",
    summary="Get my listener tags",
    response_model=SMyListenerTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyListenerTagsResponse}},
)
async def get_my_listener_tags(
    user: User = Depends(get_current_user),
) -> SMyListenerTagsResponse:
    # ???
    listener_tags = ListenerTagsDAO.find_all(listener_profile=user)
    return SMyListenerTagsResponse(tags=listener_tags)


@tags.get(
    path="/my_producer_tags",
    summary="Get my producer tags",
    response_model=SMyProducerTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyProducerTagsResponse}},
)
async def get_my_producer_tags(
    user: User = Depends(get_current_user),
) -> SMyProducerTagsResponse:
    # ???
    producer_profile = await ProducerDAO.find_one_or_none(producer_profile=user)
    if not producer_profile:
        raise NotFoundException("You don't have a producer profile")

    producer_tags = ProducerTagsDAO.find_all(producer_profile=producer_profile)
    return SMyProducerTagsResponse(tags=producer_tags)


@tags.get(
    path="/my_artist_tags",
    summary="Get my artist tags",
    response_model=SMyArtistTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyArtistTagsResponse}},
)
async def get_my_artist_tags(
    user: User = Depends(get_current_user),
) -> SMyArtistTagsResponse:
    # ???
    artist_profile = await ArtistDAO.find_one_or_none(artist_profile=user)
    if not artist_profile:
        raise NotFoundException("You don't have a artist profile")

    artist_tags = ArtistTagsDAO.find_all(user=user)
    return SMyArtistTagsResponse(tags=artist_tags)
