from abc import ABC
from dataclasses import dataclass
from io import BytesIO

import boto3

from src.core.config import settings


@dataclass
class BaseMediaRepository(ABC):
    pass


@dataclass
class S3Repository(BaseMediaRepository):
    session = boto3.Session(
        aws_access_key_id=settings.yandex_cloud.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.yandex_cloud.AWS_SECRET_ACCESS_KEY,
    )

    client = session.client(service_name="s3", endpoint_url="https://storage.yandexcloud.net")

    bucket_name = "seamusic"

    @classmethod
    async def upload_file(cls, folder, filename, file_stream: BytesIO) -> str:
        key = f"{folder}/{filename}"
        cls.client.upload_fileobj(file_stream, cls.bucket_name, key)
        file_url = f"https://storage.yandexcloud.net/{cls.bucket_name}/{key}"

        return file_url

    @classmethod
    async def delete_file(cls, folder, filename) -> None:
        key = f"{folder}/{filename}"
        cls.client.delete_object(Bucket=cls.bucket_name, Key=key)
