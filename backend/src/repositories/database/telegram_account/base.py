from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.models.subscriptions import TelegramAccount


@dataclass
class BaseTelegramAccountRepository(ABC):
    @abstractmethod
    async def add_one(self, telegram_id: int) -> None:
        ...

    @abstractmethod
    async def get_telegram_account(self, telegram_id: int) -> TelegramAccount:
        ...

    @abstractmethod
    async def get_telegram_accounts_ids(self) -> list[int]:
        ...
