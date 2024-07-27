from fastapi import APIRouter, Request
from src.subscriptions.services import TelegramAccountDAO
from typing import List
from src.subscriptions.utils import flow

subscription = APIRouter(
    prefix = "/subscription",
    tags = ["Subscription"]
)

@subscription.get('/telegram/{id}', summary='Create telegram subscription account')
async def create_telegram_account(telegram_id: int):
    telegram_account = await TelegramAccountDAO.find_one_or_none(telegram_id=telegram_id)
    if not telegram_account:
        await TelegramAccountDAO.add_one({"telegram_id": telegram_id})
        return {"message": "Telegram account created successfully"}
    return telegram_account

@subscription.get('/telegram/', summary='Create telegram subscription account')
async def get_telegram_accounts_ids() -> List[int]:
    telegram_accounts = await TelegramAccountDAO.find_all()
    telegram_ids = [telegram_account.telegram_id for telegram_account in telegram_accounts]
    return telegram_ids

@subscription.get('/auth_link', summary='Get auth link')
async def get_auth_link():
    authorization_url, state = flow.authorization_url(access_type='offline')
    return {"auth_link": authorization_url}

@subscription.get("/callback")
async def callback(request: Request):
    flow.fetch_token(authorization_response=str(request.url))

    credentials = flow.credentials
    return {"credentials": credentials}