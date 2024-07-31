from src.messages.models import Message
from src.services import SQLAlchemyRepository


class MessagesRepository(SQLAlchemyRepository):
    model = Message
