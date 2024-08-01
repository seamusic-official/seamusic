from src.models.licenses import License
from src.core.cruds import SQLAlchemyRepository


class LicensesRepository(SQLAlchemyRepository):
    model = License
