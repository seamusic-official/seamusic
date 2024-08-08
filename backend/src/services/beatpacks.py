from src.core.cruds import SQLAlchemyRepository
from src.models.beatpacks import Beatpack


class BeatpacksRepository(SQLAlchemyRepository):
    model = Beatpack
