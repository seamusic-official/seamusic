from src.subscription.models import TelegramAccount
from src.services import SQLAlchemyRepository
from src.database import async_session_maker


class TelegramAccountDAO(SQLAlchemyRepository):
    model = TelegramAccount
