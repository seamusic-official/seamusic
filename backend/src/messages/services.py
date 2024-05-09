from src.services import SQLAlchemyRepository
from src.messages.models import Message

class MessagesRepository(SQLAlchemyRepository):
    model = Message