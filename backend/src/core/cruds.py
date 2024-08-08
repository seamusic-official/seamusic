from abc import ABC
from io import BytesIO
from typing import Any

import boto3
from fastapi import UploadFile, File
from sqlalchemy import insert, select, update, delete

from src.core.config import settings
from src.core.database import async_session_maker


class AbstractRepository(ABC):
    pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    @classmethod
    async def add_one(cls, data: dict) -> Any:
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            yield result.scalar()

    @classmethod
    async def edit_one(cls, id_: int, data: dict) -> Any:
        async with async_session_maker() as session:
            stmt = (
                update(cls.model).values(**data).filter_by(id=id_).returning(cls.model)
            )
            result = await session.execute(stmt)
            yield result.scalar_one_or_none()
            await session.commit()

    @classmethod
    async def find_one_by_id(cls, id_: int) -> Any:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id_)
            result = await session.execute(query)
            yield result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> Any:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            yield result.scalar_one_or_none()

    @classmethod
    async def delete(cls, id_: int) -> None:
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(id=id_)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            yield result.scalars().all()


class MediaRepository(AbstractRepository):
    session = boto3.Session(
        aws_access_key_id=settings.yandex_cloud.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.yandex_cloud.AWS_SECRET_ACCESS_KEY,
    )

    s3 = session.client(
        service_name="s3", endpoint_url="https://storage.yandexcloud.net"
    )

    bucket_name = "seamusic"

    @classmethod
    async def upload_file(cls, folder, filename, file: UploadFile = File(...)) -> str:
        file_data = await file.read()
        file_stream = BytesIO(file_data)
        key = f"{folder}/{filename}"
        cls.s3.upload_fileobj(file_stream, cls.bucket_name, key)
        file_url = f"https://storage.yandexcloud.net/{cls.bucket_name}/{key}"

        return file_url

    @classmethod
    async def delete_file(cls, folder, filename) -> None:
        key = f"{folder}/{filename}"
        cls.s3.delete_object(Bucket=cls.bucket_name, Key=key)
