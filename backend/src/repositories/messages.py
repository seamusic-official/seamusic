from src.core.cruds import SQLAlchemyRepository
from src.models.messages import Message


class MessagesRepository(SQLAlchemyRepository):
    model = Message
