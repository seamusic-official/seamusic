from io import BytesIO

import boto3
from fastapi import UploadFile, File

from src.core.config import settings


class MediaRepository:
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
