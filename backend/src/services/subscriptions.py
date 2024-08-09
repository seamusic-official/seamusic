from src.exceptions.services import NotFoundException
from src.models.subscriptions import TelegramAccount
from src.repositories.subscriptions import TelegramAccountDAO


class SubscriptionsService:
    @staticmethod
    async def create_telegram_account(telegram_id: int) -> TelegramAccount:
        return await TelegramAccountDAO.add_one({"telegram_id": telegram_id})

    @staticmethod
    async def get_telegram_account(telegram_id: int) -> TelegramAccount:
        telegram_account = await TelegramAccountDAO.find_one_or_none(telegram_id=telegram_id)

        if not telegram_account:
            raise NotFoundException("Account not found")

        return telegram_account

    @staticmethod
    async def get_telegram_accounts_ids() -> list[int]:
        telegram_accounts = await TelegramAccountDAO.find_all()
        return list(map(lambda telegram_account: telegram_account.telegram_id, telegram_accounts))
