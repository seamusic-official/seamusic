from src.beats.models import Beat
from src.services import SQLAlchemyRepository
from src.config import settings


class SoundkitRepository(SQLAlchemyRepository):
    model = Beat