from src.core.cruds import SQLAlchemyRepository
from src.models.licenses import License


class LicensesRepository(SQLAlchemyRepository):
    model = License
