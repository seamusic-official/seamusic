from src.services import SQLAlchemyRepository
from src.models.soundkits import Soundkit


class SoundkitRepository(SQLAlchemyRepository):
    model = Soundkit
