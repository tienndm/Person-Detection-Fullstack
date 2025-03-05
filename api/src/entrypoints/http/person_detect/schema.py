from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class RecordResponse(BaseModel):
    id: int
    personCount: int
    outputSaveDir: str
    createdAt: datetime