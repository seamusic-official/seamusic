from dataclasses import dataclass

from sqlalchemy import select

from src.models.subscriptions import TelegramAccount
from src.repositories.converters.sqlalchemy import request_dto_to_model, model_to_response_dto
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.telegram_account.base import BaseTelegramAccountRepository
from src.repositories.dtos.subscriptions import (
    TelegramAccountResponseDTO,
    TelegramAccountsIDSResponseDTO,
    CreateTelegramAccountRequestDTO
)


@dataclass
class TelegramAccountRepository(SQLAlchemyRepository, BaseTelegramAccountRepository):
    async def add_one(self, telegram_account: CreateTelegramAccountRequestDTO) -> None:
        telegram_account = request_dto_to_model(request_dto=telegram_account, model=TelegramAccount)
        self.session.add(telegram_account)

    async def get_telegram_account_by_id(self, telegram_id: int) -> TelegramAccountResponseDTO | None:
        query = select(TelegramAccount).filter_by(telegram_id=telegram_id)
        return model_to_response_dto(model=await self.session.scalar(query), response_dto=TelegramAccountResponseDTO)

    async def get_telegram_accounts_ids(self) -> TelegramAccountsIDSResponseDTO:
        query = select(TelegramAccount).column(column='telegram_id')
        ids = list(await self.session.scalar(query))
        return TelegramAccountsIDSResponseDTO(ids=ids)
