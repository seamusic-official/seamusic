from src.beatpacks.models import BeatPack
from src.services import SQLAlchemyRepository

class BeatpacksRepository(SQLAlchemyRepository):
    model = BeatPack