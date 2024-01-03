from abc import ABC
from sqlalchemy import insert, select, update, delete, desc
from database import async_session_maker

class AbstractRepository(ABC):
    pass


class SQLAlchemyRepository(AbstractRepository):
    model = None
    
    @classmethod
    async def add_one(cls, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()
            return stmt

    @classmethod
    async def edit_one(cls, id: int, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = update(cls.model).values(**data).filter_by(id=id).returning(cls.model.id)
            await session.execute(stmt)
            await session.commit()
            return stmt

    @classmethod
    async def find_one_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.first()
    
    @classmethod
    async def delete(cls, id: int) -> None:
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(id=id)
            await session.execute(stmt)
            await session.commit()
            return {"success": "ok"}
    
    @classmethod
    async def find_all(cls, **filter_by) -> list:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()       
