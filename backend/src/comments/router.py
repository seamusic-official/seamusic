from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends, HTTPException
from .models import BaseComment
from .schemas import CommentCreate, CommentResponse, CommentUpdate
from src.database import get_async_session
from src.beats.models import Beat
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy.orm import joinedload
from src.beatpacks.models import Beatpack
from src.soundkits.models import Soundkit

comments = APIRouter(prefix="/comments", tags=["Comments"])


@comments.post("/create-comment-for-beat/{beat_id}/")
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
    "/get-comments-from-beats/{beat_id}/", response_model=List[CommentResponse]
)
async def get_comments_from_beats(
    beat_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
) -> List[CommentResponse] | None:

    beat_result = await session.execute(select(Beat).filter(Beat.id == beat_id))

    beat = beat_result.scalars().first()
    if not beat:
        raise HTTPException(detail="Not found", status_code=404)

    comments = await session.execute(
        select(BaseComment)
        .filter(BaseComment.beat_id == beat_id)
        .order_by(BaseComment.created_at.desc())
        .options(joinedload(BaseComment.comment_author))
    )

    comment_result = comments.scalars().all()
    if not comment_result:
        raise HTTPException(detail="Not Found", status_code=404)

    return comment_result


@comments.delete("/delete-comment/{comment_id}/")
async def delete(
    commemnt_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
):

    comment = await session.execute(
        select(BaseComment)
        .filter(BaseComment.id == commemnt_id)
        .filter(BaseComment.comment_creator_id == current_user.id)
    )

    comment_result = comment.scalars().first()
    if comment_result:
        await session.delete(comment_result)
        await session.commit()
        return "Bro Your Comment Deleted SuccsesFully"
    else:
        raise HTTPException(detail="Bro Comment not found", status_code=404)


@comments.put("/update-comment/{comment_id}/", response_model=CommentUpdate)
async def update(
    request: CommentUpdate,
    comment_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
):

    comment = await session.execute(
        select(BaseComment)
        .filter(BaseComment.id == comment_id)
        .filter(BaseComment.comment_creator_id == current_user.id)
    )

    comment_result = comment.scalars().first()
    if not comment_result:
        raise HTTPException(
            detail=f"Bro I am sorry but comment with id {comment_id} not found",
            status_code = 404
        )

    comment_result.comment = request.comment
    await session.commit()
    return comment_result


@comments.post("/create-comment-for-beatpack/{beatpack_id}/")
async def create_comment_for_beatpack(
    request: CommentCreate,
    beatpack_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
):

    beatpack_result = await session.execute(
        select(Beatpack).filter(Beatpack.id == beatpack_id)
    )

    beatpack = beatpack_result.scalars().first()
    if not beatpack:
        raise HTTPException(
            detail=f"Bro Beat with id {beatpack_id} not found", status_code=404
        )

    new_comment = BaseComment(
        comment=request.comment,
        comment_creator_id=current_user.id,
        beat_pack_id=beatpack.id,
    )

    session.add(new_comment)
    await session.commit()
    return new_comment


@comments.get(
    "/get-comments-from-beatpacks/{beatpack_id}/", response_model=List[CommentResponse]
)
async def get_comments_from_beatpack(
    beat_pack_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
) -> List[CommentResponse] | None:

    beatpack_result = await session.execute(
        select(Beatpack).filter(Beatpack.id == beat_pack_id)
    )

    beat = beatpack_result.scalars().first()
    if not beat:
        raise HTTPException(detail="Not found", status_code=404)

    comments = await session.execute(
        select(BaseComment)
        .filter(BaseComment.beat_pack_id == beat_pack_id)
        .order_by(BaseComment.created_at.desc())
        .options(joinedload(BaseComment.comment_author))
    )

    comment_result = comments.scalars().all()
    if not comment_result:
        raise HTTPException(detail="Not Found", status_code=404)

    return comment_result


@comments.post("/create-comment-for-soundkit/{soundkit_id}/")
async def create_comment_for_beatpack(
    request: CommentCreate,
    soundkit_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
):

    soundkit_result = await session.execute(
        select(Soundkit).filter(Soundkit.id == soundkit_id)
    )

    soundkit = soundkit_result.scalars().first()
    if not soundkit:
        raise HTTPException(
            detail=f"Bro Beat with id {soundkit_id} not found", status_code=404
        )

    new_comment = BaseComment(
        comment=request.comment,
        comment_creator_id=current_user.id,
        soundkit_id=soundkit.id,
    )

    session.add(new_comment)
    await session.commit()
    return new_comment


@comments.get(
    "/get-comments-from-soundkits/{soundkits_id}/", response_model=List[CommentResponse]
)
async def get_comments_from_beatpack(
    soundkits_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: SUser = Depends(get_current_user),
) -> List[CommentResponse] | None:

    soundkit_result = await session.execute(
        select(Soundkit).filter(Soundkit.id == soundkits_id)
    )

    beat = soundkit_result.scalars().first()
    if not beat:
        raise HTTPException(detail="Not found", status_code=404)

    comments = await session.execute(
        select(BaseComment)
        .filter(BaseComment.soundkit_id == soundkits_id)
        .order_by(BaseComment.created_at.desc())
        .options(joinedload(BaseComment.comment_author))
    )

    comment_result = comments.scalars().all()
    if not comment_result:
        raise HTTPException(detail="Not Found", status_code=404)

    return comment_result




