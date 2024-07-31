from src.services import SQLAlchemyRepository
from src.models.tracks import Track


class TracksRepository(SQLAlchemyRepository):
    model = Track
