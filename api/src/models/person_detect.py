from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from common.type import UUIDStr


@dataclass
class RecordModel:
    personCount: int
    imageUUID: UUIDStr
    id: Optional[int] = None
    createdAt: Optional[str] = None


@dataclass
class TotalPageModel:
    totalPage: int


@dataclass
class GetRecordParamsModel:
    page: int = 1
    size: int = 10
