from src.core.cruds import SQLAlchemyRepository
from src.models.squads import Squad


class SquadRepository(SQLAlchemyRepository):
    model = Squad
