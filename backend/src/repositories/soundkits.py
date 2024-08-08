from src.core.cruds import SQLAlchemyRepository
from src.models.soundkits import Soundkit


class SoundkitRepository(SQLAlchemyRepository):
    model = Soundkit
