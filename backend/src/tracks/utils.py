import os
import uuid

from fastapi import HTTPException, UploadFile


async def unique_track_filename(file: UploadFile) -> str:
    try:
        file_name, file_extension = os.path.splitext(file.filename)
        unique_filename = (
            f"track-{file_name.replace(' ', '-')}_{uuid.uuid4()}{file_extension}"
        )
        return unique_filename

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to process the audio file: {str(e)}"
        )
