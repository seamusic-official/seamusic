from fastapi import APIRouter
from src.subscription.services import TelegramAccountDAO



subscription = APIRouter(
    prefix = "/subscription",
    tags = ["Subscription"]
)

@subscription.get('/telegram/{id}', summary='Create telegram subcription account')
async def create_telegram_account(id: int):
    # ???
    user = await TelegramAccountDAO.find_one_or_none(telegram_id=id)
    if not user:
        return await TelegramAccountDAO.add_one(telegram_id=id)

@subscription.get('/telegram/{id}', summary='Create telegram subcription account')
async def create_telegram_account(id):
    # ???
    user = TelegramAccountDAO.find_one_or_none(telegram_id=id)
    if not user:
        return await TelegramAccountDAO.add_one(telegram_id=id)