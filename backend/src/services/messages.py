from src.models.messages import Message
from src.services import SQLAlchemyRepository


class MessagesRepository(SQLAlchemyRepository):
    model = Message
