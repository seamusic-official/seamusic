from fastapi import APIRouter

from src.services.messages import MessagesRepository


messages = APIRouter(prefix="/messages", tags=["Messages"])


