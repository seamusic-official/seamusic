from dataclasses import dataclass
from boto3 import Session, client
from io import BytesIO

from src.core.config import settings
from src.repositories import BaseMediaRepository


@dataclass
class S3Repository(BaseMediaRepository):
    _client: client
    bucket_name: str


    async def upload_file(self, folder: str, filename: str, file_stream: BytesIO) -> str:
        key = f"{folder}/{filename}"
        self._client.upload_fileobj(file_stream, self.bucket_name, key)
        file_url = f"https://storage.yandexcloud.net/{self.bucket_name}/{key}"

        return file_url


    async def delete_file(self, folder: str, filename: str) -> None:
        key = f"{folder}/{filename}"
        self._client.delete_object(Bucket=self.bucket_name, Key=key)


def init_s3_client() -> client:
    session = Session(
        aws_access_key_id=settings.yandex_cloud.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.yandex_cloud.AWS_SECRET_ACCESS_KEY,
    )
    return session.client(service_name="s3", endpoint_url="https://storage.yandexcloud.net")

def init_s3_repository() -> BaseMediaRepository:
    return S3Repository(
        _client=init_s3_client(),
        bucket_name=settings.s3.BUCKET_NAME
    )

