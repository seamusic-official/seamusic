import os
import re
import uuid

from fastapi import UploadFile, HTTPException


async def unique_filename(file: UploadFile) -> str:
    try:
        file_name, file_extension = os.path.splitext(file.filename)
        file_name_cleaned = re.sub(r'[^\w\s-]', '_', file_name)
        unique_filename_ = f"beat-{file_name_cleaned.replace(' ', '-')}_{uuid.uuid4()}{file_extension}"

        return unique_filename_

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process the audio file: {str(e)}")
