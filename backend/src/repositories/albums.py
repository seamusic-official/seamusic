from src.core.cruds import SQLAlchemyRepository
from src.models.albums import Album


class AlbumsRepository(SQLAlchemyRepository):
    model = Album
