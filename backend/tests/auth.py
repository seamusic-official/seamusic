from typing import AsyncGenerator
from src.database import create_async_engine, AsyncSession, sessionmaker
from src.config import DbSettings
import pytest
from src.main import app
from sqlalchemy.pool import NullPool
from src.database import get_async_session, metadata
import asyncio
from httpx import AsyncClient

DATABASE_URL = DbSettings.url

engine_test = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)

    yield

    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)

@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
