from typing import Optional, List

from pydantic import BaseModel

from src.schemas.base import BaseResponse


class TelegramAccount(BaseModel):
    telegram_id: Optional[int] = None
    subscribe: Optional[int] = None


class OnlyTelegramSubscribeMonth(BaseModel):
    subscribe: Optional[bool] = None
    telegram_account_id: int
    telegram_account: TelegramAccount


class OnlyTelegramSubscribeYear(BaseModel):
    subscribe: Optional[bool] = None
    telegram_account_id: Optional[int] = None
    telegram_account: TelegramAccount


class SCreateTelegramAccountResponse(BaseResponse):
    telegram_id: Optional[int] = None
    subscribe: Optional[bool] = None
    only_telegram_subscribe_year: OnlyTelegramSubscribeYear
    only_telegram_subscribe_month: OnlyTelegramSubscribeMonth


class STelegramAccountsIDResponse(BaseResponse):
    ids: List[int]
