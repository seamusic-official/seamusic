from fastapi import UploadFile
import os
import shutil
import uuid
import aiofiles
from fastapi import HTTPException
from mutagen.mp3 import MP3
from mutagen.wavpack import WavPack


async def save_image(upload_folder: str, file: UploadFile):
    try:
        file_name, file_extension = os.path.splitext(file.filename)
        unique_filename = f"{file_name}-{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(upload_folder, unique_filename)

        async with aiofiles.open(file_path, "wb") as buffer:
            await buffer.write(await file.read())

        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading image: {str(e)}")


async def save_audio(upload_folder: str, file: UploadFile) -> dict:
    try:
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        allowed_formats = [".mp3", ".wav"]
        file_name, file_extension = os.path.splitext(file.filename)

        if file_extension not in allowed_formats:
            raise HTTPException(
                status_code=400, detail="Only MP3 and WAV files are allowed."
            )

        unique_filename = f"{file_name}-{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(upload_folder, unique_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get file info
        file_info = dict()
        file_info["file_path"] = unique_filename

        if file_extension == ".mp3":
            audio = MP3(file_path)
            file_info["title"] = str(audio.get("TIT2", "Unknown Title"))
            file_info["artist"] = str(audio.get("TPE1", "Unknown Artist"))
        elif file_extension == ".wav":
            audio = WavPack(file_path)
            file_info["title"] = str(audio.get("title", "Unknown Title"))
            file_info["artist"] = str(audio.get("artist", "Unknown Artist"))

        return file_info

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error uploading audio file: {str(e)}"
        )
