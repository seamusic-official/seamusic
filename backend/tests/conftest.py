import asyncio
from datetime import datetime
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient, Response
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.auth.schemas import SUserLoginResponse, SUserResponse, SRegisterUser, Role, SLoginUser
from src.config import settings
from src.database import get_async_session
from src.main import app
from src.tags.schemas import STag


DATABASE_URL_TEST = f'postgresql+asyncpg://{settings.db.DB_USER_TEST}:{settings.db.DB_PASS_TEST}@{settings.db.DB_HOST_TEST}:{settings.db.DB_PORT_TEST}/{settings.db.DB_NAME_TEST}'
engine_test = create_async_engine(DATABASE_URL_TEST, echo=True)
async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)

_client = TestClient(app=app)
email = 'test_email@example.com'
password = 'test_password'


user = SRegisterUser(
    username='test_username',
    password=password,
    email=email,
    roles=[Role.listener, Role.superuser, Role.moder, Role.producer, Role.listener],
    birthday=None,
    tags=[STag(name='supertrap'), STag(name='newjazz'), STag(name='rage'), STag(name='hyperpop')]
)
_client.post(url='/auth/register', json=user.model_dump())


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    is_available: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(scope='session')
def client() -> TestClient:
    return _client


def login(email_: str, password_: str) -> SUserResponse:
    response: Response = _client.post(
        url='/auth/login',
        json=SLoginUser(email=email_, password=password_).model_dump()
    )
    return SUserLoginResponse(**response.json()).user


@pytest.fixture(scope='session')
def user(client: TestClient) -> SUserResponse:
    return login(email_=email, password_=password)


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    '''Create an instance of the default event loop for each test case.'''
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
