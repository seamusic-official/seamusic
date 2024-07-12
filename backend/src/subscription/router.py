from fastapi import UploadFile, File, APIRouter, Depends, HTTPException, Response
from typing import List
from src.subscription.services import TelegramAccountDAO
from src.config import settings
from src.beats.utils import unique_filename


subscription = APIRouter(
    prefix = "/subscription",
    tags = ["Subscription"]
)

@subscription.get('/telegram/{id}', summary='Create telegram subcription account')
async def create_telegram_account(id: int):
    user = await TelegramAccountDAO.find_one_or_none(telegram_id=id)
    if not user:
        return await TelegramAccountDAO.add_one(telegram_id=id)

@subscription.get('/telegram/{id}', summary='Create telegram subcription account')
async def create_telegram_account(id):
    user = TelegramAccountDAO.find_one_or_none(telegram_id=id)
    if not user:
        return await TelegramAccountDAO.add_one(telegram_id=id)