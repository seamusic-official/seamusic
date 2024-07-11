import os
import uuid
import re
from fastapi import UploadFile, HTTPException

async def unique_filename(file: UploadFile) -> str:
    try:
        file_name, file_extension = os.path.splitext(file.filename)
        
        # Replace special characters with underscores
        file_name_cleaned = re.sub(r'[^\w\s-]', '_', file_name)

        unique_filename = f"beat-{file_name_cleaned.replace(' ', '-')}_{uuid.uuid4()}{file_extension}"

        return unique_filename

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process the audio file: {str(e)}")
