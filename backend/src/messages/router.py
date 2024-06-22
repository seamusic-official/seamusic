from fastapi import APIRouter, HTTPException
from src.messages.services import MessagesRepository 


messages = APIRouter(
    prefix = "/messages",
    tags = ["Messages"]
)

@messages.get("/my/", summary="Create new messages")
async def get_spotify_tracks():
    return MessagesRepository.get_tracks()
