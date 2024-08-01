from src.models.albums import Album
from src.core.cruds import SQLAlchemyRepository


class AlbumsRepository(SQLAlchemyRepository):
    model = Album
