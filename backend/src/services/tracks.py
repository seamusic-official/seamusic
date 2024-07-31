from src.core.cruds import SQLAlchemyRepository
from src.models.tracks import Track


class TracksRepository(SQLAlchemyRepository):
    model = Track
