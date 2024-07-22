from src.licenses.models import License
from src.services import SQLAlchemyRepository

    
class LicensesRepository(SQLAlchemyRepository):
    model = License
    