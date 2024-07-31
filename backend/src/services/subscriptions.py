from src.services import SQLAlchemyRepository
from src.models.subscriptions import TelegramAccount


class TelegramAccountDAO(SQLAlchemyRepository):
    model: "TelegramAccount"
