from fastapi import APIRouter, status, HTTPException

from src.schemas.subscriptions import STelegramAccountsIDResponse, STelegramAccountResponse
from src.repositories.subscriptions import TelegramAccountDAO

subscription = APIRouter(
    prefix="/subscription", tags=["Subscription"], include_in_schema=False
)


@subscription.post(
    path="/telegram",
    summary="Create telegram subscription account",
    response_model=STelegramAccountResponse,
    responses={status.HTTP_201_CREATED: {"model": STelegramAccountResponse}},
)
async def create_telegram_account(telegram_id: int) -> STelegramAccountResponse:
    telegram_account = await TelegramAccountDAO.add_one({"telegram_id": telegram_id})

    return telegram_account


@subscription.get(
    path="/telegram/{id}",
    summary="Get telegram subscription account",
    response_model=STelegramAccountResponse,
    responses={status.HTTP_200_OK: {"model": STelegramAccountResponse}},
)
async def get_telegram_account(telegram_id: int) -> STelegramAccountResponse:
    telegram_account = await TelegramAccountDAO.find_one_or_none(
        telegram_id=telegram_id
    )

    if not telegram_account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )

    return telegram_account


@subscription.get(path="/telegram/", summary="Create telegram subscription account")
async def get_telegram_accounts_ids() -> STelegramAccountsIDResponse:
    telegram_accounts = TelegramAccountDAO.find_all()
    telegram_ids = [
        telegram_account.telegram_id for telegram_account in telegram_accounts
    ]
    return STelegramAccountsIDResponse(ids=telegram_ids)
