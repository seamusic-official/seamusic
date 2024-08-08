import os
import uuid
from io import BytesIO

from fastapi import HTTPException, UploadFile


def unique_filename(file: UploadFile) -> str:
    try:
        file_name, file_extension = os.path.splitext(file.filename)
        return f'track-{file_name.replace(" ", "-")}_{uuid.uuid4()}{file_extension}'

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process the audio file: {str(e)}")


async def get_file_stream(file: UploadFile) -> BytesIO:
    file_data = await file.read()
    return BytesIO(file_data)
