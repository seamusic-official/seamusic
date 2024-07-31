from src.services import SQLAlchemyRepository
from src.subscriptions.models import TelegramAccount


class TelegramAccountDAO(SQLAlchemyRepository):
    model: "TelegramAccount"
