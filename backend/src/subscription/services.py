from src.subscription.models import TelegramAccount
from src.services import SQLAlchemyRepository


class TelegramAccountDAO(SQLAlchemyRepository):
    model = TelegramAccount
