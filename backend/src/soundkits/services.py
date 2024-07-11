from src.soundkits.models import Soundkit
from src.services import SQLAlchemyRepository
from src.config import settings


class SoundkitRepository(SQLAlchemyRepository):
    model = Soundkit