from dataclasses import dataclass

from src.dtos.database.subscriptions import CreateTelegramAccountRequestDTO, TelegramAccountResponseDTO
from src.exceptions.services import NotFoundException
from src.repositories import DatabaseRepositories, Repositories
from src.repositories.database.telegram_account.base import BaseTelegramAccountRepository


@dataclass
class TelegramAccountDatabaseRepositories(DatabaseRepositories):
    telegram_account: BaseTelegramAccountRepository


@dataclass
class SubscriptionsRepositories(Repositories):
    database: TelegramAccountDatabaseRepositories


class SubscriptionsService:
    repositories: SubscriptionsRepositories

    async def create_telegram_account(self, telegram_id: int) -> int:
        telegramm_account = CreateTelegramAccountRequestDTO(id=telegram_id)
        return await self.repositories.database.telegram_account.add_one(telegram_account=telegramm_account)

    async def get_telegram_account(self, telegram_id: int) -> TelegramAccountResponseDTO | None:
        telegram_account = await self.repositories.database.telegram_account.get_telegram_account_by_id(telegram_id=telegram_id)

        if not telegram_account:
            raise NotFoundException("Account not found")

        return telegram_account

    async def get_telegram_accounts_ids(self) -> list[int]:
        telegram_accounts = await self.repositories.database.telegram_account.get_telegram_accounts_ids()
        return list(map(lambda telegram_account: telegram_account.telegram_id, telegram_accounts))
