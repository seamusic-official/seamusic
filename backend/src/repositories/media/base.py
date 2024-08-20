from abc import ABC
from dataclasses import dataclass
from io import BytesIO


@dataclass
class BaseMediaRepository(ABC):
    async def upload_file(self, folder: str, filename: str, file_stream: BytesIO) -> str:
        ...

    async def delete_file(self, folder: str, filename: str) -> None:
        ...
