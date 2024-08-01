from src.models.beatpacks import Beatpack
from src.core.cruds import SQLAlchemyRepository


class BeatpacksRepository(SQLAlchemyRepository):
    model = Beatpack
