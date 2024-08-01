from fastapi import APIRouter

from src.services.messages import MessagesRepository


messages = APIRouter(prefix="/messages", tags=["Messages"])


@messages.get(path="/my/", summary="Create new messages")
async def get_spotify_tracks():
    # ????
    return MessagesRepository.get_tracks()
