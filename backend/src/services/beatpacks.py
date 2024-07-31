from src.models.beatpacks import Beatpack
from src.services import SQLAlchemyRepository


class BeatpacksRepository(SQLAlchemyRepository):
    model = Beatpack
