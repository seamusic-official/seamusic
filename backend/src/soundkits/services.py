from src.services import SQLAlchemyRepository
from src.soundkits.models import Soundkit


class SoundkitRepository(SQLAlchemyRepository):
    model = Soundkit
