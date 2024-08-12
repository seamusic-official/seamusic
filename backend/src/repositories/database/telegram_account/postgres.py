from dataclasses import dataclass

from sqlalchemy import select

from src.models.subscriptions import TelegramAccount
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.telegram_account.base import BaseTelegramAccountRepository


@dataclass
class TelegramAccountRepository(SQLAlchemyRepository, BaseTelegramAccountRepository):
    async def add_one(self, telegram_id: int) -> None:
        telegram_account = TelegramAccount(telegram_id=telegram_id)
        self.session.add(telegram_account)

    async def get_telegram_account(self, telegram_id: int) -> TelegramAccount:
        query = select(TelegramAccount).filter_by(telegram_id=telegram_id)
        return await self.session.scalar(query)

    async def get_telegram_accounts_ids(self) -> list[int]:
        query = select(TelegramAccount).column(column='telegram_id')
        return list(await self.session.scalar(query))
