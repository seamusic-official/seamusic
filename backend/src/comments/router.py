from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.auth.dependencies import get_current_user
from src.auth.schemas import SUser
from src.beats.models import Beat
from src.comments.models import BaseComment
from src.comments.schemas import (
    CommentCreate,
    CommentResponse,
    CommentUpdate,
    SCommentDeleteResponse,
    CommentUpdateResponse,
)
from src.database import get_async_session


comments = APIRouter(prefix="/comments", tags=["Comments"])


@comments.post(
    path="/create-comment-for-beat/{beat_id}/", summary="create comment for beat"
)
async def create_comment_for_beat(
    beat_id: int,
    request: CommentCreate,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
):

    beat_result = await session.execute(select(Beat).filter(Beat.id == beat_id))

    beat = beat_result.scalars().first()
    if not beat:
        raise HTTPException(
            detail=f"Bro Beat with id {beat_id} not found", status_code=404
        )

    new_comment = BaseComment(
        comment=request.comment, comment_creator_id=current_user.id, beat_id=beat.id
    )

    session.add(new_comment)
    await session.commit()
    return new_comment


@comments.get(
    path="/get-comments_-from-beats/{beat_id}/",
    response_model=List[CommentResponse],
    responses={status.HTTP_200_OK: {"model": List[CommentResponse]}},
)
async def get_comments_from_beats(
    beat_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> List[CommentResponse] | None:

    beat_result = await session.execute(select(Beat).filter(Beat.id == beat_id))

    beat = beat_result.scalars().first()
    if not beat:
        raise HTTPException(detail="Not found", status_code=404)

    comments_ = await session.execute(
        select(BaseComment)
        .filter(BaseComment.beat_id == beat_id)
        .order_by(BaseComment.created_at.desc())
        .options(joinedload(BaseComment.comment_author))
    )

    comment_result = comments_.scalars().all()
    if not comment_result:
        raise HTTPException(detail="Not Found", status_code=404)

    return comment_result


@comments.delete(
    path="/delete-comment/{comment_id}/",
    summary="delete comment by id",
    response_model=SCommentDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SCommentDeleteResponse}},
)
async def delete(
    commemnt_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
) -> SCommentDeleteResponse:

    comment = await session.execute(
        select(BaseComment)
        .filter(BaseComment.id == commemnt_id)
        .filter(BaseComment.comment_creator_id == current_user.id)
    )

    comment_result = comment.scalars().first()
    if comment_result:
        await session.delete(comment_result)
        await session.commit()
        return SCommentDeleteResponse
    else:
        raise HTTPException(detail="Bro Comment not found", status_code=404)


@comments.put(
    path="/update-comment/{comment_id}/",
    response_model=CommentUpdateResponse,
    responses={status.HTTP_200_OK: {"model": CommentUpdateResponse}},
)
async def update(
    request: CommentUpdate,
    comment_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
) -> CommentUpdateResponse:

    comment = await session.execute(
        select(BaseComment)
        .filter(BaseComment.id == comment_id)
        .filter(BaseComment.comment_creator_id == current_user.id)
    )

    comment_result = comment.scalars().first()
    if not comment_result:
        raise HTTPException(
            detail=f"Bro I am sorry but comment with id {comment_id} not found",
            status_code=404,
        )

    comment_result.comment = request.comment
    await session.commit()
    return CommentUpdateResponse
