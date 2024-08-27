from io import BytesIO
import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from src.utils.files import get_file_stream, unique_filename


class MockUploadFile:
    def init(self, filename: str):
        self.filename = filename

    async def read(self):
        return b'This is dummy data for file reading.'


def test_unique_filename_with_valid_file():
    mock_file = MockUploadFile("my audio file.mp3")
    result = unique_filename(mock_file)
    assert result.startswith("track-my-audio-file_")
    assert result.endswith(".mp3")


def test_unique_filename_with_no_file():
    result = unique_filename()
    assert result is None


def test_unique_filename_with_invalid_file():
    mock_file = MockUploadFile("invalid file")  # A valid name but for testing error handling
    
    try:
        unique_filename(mock_file)
    except HTTPException as e:
        assert e.status_code == 500
        assert "Failed to process the audio file" in e.detail


@pytest.mark.asyncio
async def test_get_file_stream():
    mock_file = MockUploadFile("dummyfile.txt")
    file_stream = await get_file_stream(mock_file)
    assert isinstance(file_stream, BytesIO)
    assert file_stream.getvalue() == b'This is dummy data for file reading.'


@pytest.mark.asyncio
async def test_get_file_stream_empty_file():
    empty_file = MockUploadFile("emptyfile.txt")
    empty_file.read = MagicMock(return_value=b'')
    file_stream = await get_file_stream(empty_file)
    assert isinstance(file_stream, BytesIO)
    assert file_stream.getvalue() == b''