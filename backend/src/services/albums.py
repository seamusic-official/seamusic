from src.models.albums import Album
from src.services import SQLAlchemyRepository


class AlbumsRepository(SQLAlchemyRepository):
    model = Album
