from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from src.config import settings
from sqlalchemy.orm import Mapped, session
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy import func, text, Column
from sqlalchemy.dialects.postgresql import TIMESTAMP
from typing import AsyncGenerator
from sqlalchemy import MetaData

metadata = MetaData()



engine = create_async_engine(
    settings.db.url,
    echo=True
)

async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    
    is_available: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now)
    
    def __repr__(self):
        values = ', '.join(f"{col.name}={getattr(self, col.name)}" for col in self.__table__.columns[:6])
        return f"<{self.__class__.__name__}({values})>"
    


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session