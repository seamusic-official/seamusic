from src.soundkits.models import Soundkit
from src.services import SQLAlchemyRepository


class SoundkitRepository(SQLAlchemyRepository):
    model = Soundkit