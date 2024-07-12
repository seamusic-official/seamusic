from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional, List

class STag(BaseModel):
    name: str