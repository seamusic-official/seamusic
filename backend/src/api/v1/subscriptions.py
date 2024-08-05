from typing import Union

from fastapi import APIRouter, status

from src.schemas.base import BaseResponse
from src.schemas.subscriptions import STelegramAccountsIDResponse, SCreateTelegramAccountResponse
from src.services.subscriptions import TelegramAccountDAO


subscription = APIRouter(prefix="/subscription", tags=["Subscription"], include_in_schema=False)


@subscription.get(
    path="/telegram/{id}",
    summary="Create telegram subscription account",
    response_model=SCreateTelegramAccountResponse,
    responses={status.HTTP_200_OK: {"model": SCreateTelegramAccountResponse}}
)
async def create_telegram_account(telegram_id: int) -> Union[SCreateTelegramAccountResponse, BaseResponse]:
    telegram_account = await TelegramAccountDAO.find_one_or_none(
        telegram_id=telegram_id
    )
    if not telegram_account:
        await TelegramAccountDAO.add_one({"telegram_id": telegram_id})
        return BaseResponse(message="Telegram account created successfully")
    return telegram_account


@subscription.get(path="/telegram/", summary="Create telegram subscription account")
async def get_telegram_accounts_ids() -> STelegramAccountsIDResponse:
    telegram_accounts = TelegramAccountDAO.find_all()
    telegram_ids = [
        telegram_account.telegram_id for telegram_account in telegram_accounts
    ]
    return STelegramAccountsIDResponse(ids=telegram_ids)
