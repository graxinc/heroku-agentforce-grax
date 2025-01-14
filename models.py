from datetime import datetime, UTC
from sqlalchemy import Column, Integer, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Interaction(Base):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    logs = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))