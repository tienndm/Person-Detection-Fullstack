from .base_postgre import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone, timedelta  # Added timedelta

class Core(Base):
    __tablename__ = "core"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now(tz=timezone(timedelta(hours=7))))  # Updated timezone
    person_count = Column(Integer, nullable=False)
    input_save_dir = Column(String(255), nullable=False)
    output_save_dir = Column(String(255), nullable=False)
