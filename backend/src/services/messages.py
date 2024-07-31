from src.models.messages import Message
from src.core.cruds import SQLAlchemyRepository


class MessagesRepository(SQLAlchemyRepository):
    model = Message
