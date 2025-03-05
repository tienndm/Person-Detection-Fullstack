from datetime import datetime
from sqlalchemy import Integer, String, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from common.type import UUIDStr
from common.utils import build_uui4_str


class Base(DeclarativeBase):
    pass


class PersonDetect(Base):
    __tablename__ = "person_detect"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    person_count: Mapped[int] = mapped_column(Integer, nullable=False)
    image_uuid: Mapped[UUIDStr] = mapped_column(String(32), nullable=False)
    createdAt: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )
