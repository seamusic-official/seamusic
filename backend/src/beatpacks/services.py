from src.beatpacks.models import Beatpack
from src.services import SQLAlchemyRepository

class BeatpacksRepository(SQLAlchemyRepository):
    model = Beatpack