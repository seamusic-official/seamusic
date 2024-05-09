from src.auth.models import User, ProducerProfile, ArtistProfile
from src.services import SQLAlchemyRepository
from src.database import async_session_maker
from sqlalchemy import insert, select, update, delete, desc

class UsersDAO(SQLAlchemyRepository):
    model = User
    
    @classmethod
    async def find_all_artists(cls):
        async with async_session_maker() as session:
            query = select(cls.model).filter(cls.model.artist_profile != None)
            result = await session.execute(query)
            return result.scalars().all()
        
class ProducerDAO(SQLAlchemyRepository):
    model = ProducerProfile

class ArtistDAO(SQLAlchemyRepository):
    model = ArtistProfile

