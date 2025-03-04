from datetime import datetime, timezone
from typing import List
from pydantic import BaseModel

class DetectBaseSchema(BaseModel):
    id: int 
    timestamp: datetime
    person_count: int
    input_save_dir: str
    output_save_dir: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True