from typing import Any

from sqlalchemy import insert, select, update, delete

from src.core.database import async_session_maker


class SQLAlchemyRepository:
    model = None

    @classmethod
    async def add_one(cls, data: dict) -> object:
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
        return result.scalar()

    @classmethod
    async def edit_one(cls, id_: int, data: dict) -> object:
        async with async_session_maker() as session:
            stmt = (
                update(cls.model).values(**data).filter_by(id=id_).returning(cls.model)
            )
            result = await session.execute(stmt)
            await session.commit()
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_by_id(cls, id_: int) -> object:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id_)
            result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> object:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def delete(cls, id_: int) -> None:
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(id=id_)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def find_all(cls, **filter_by) -> list[object]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
        return result.scalars().all()
