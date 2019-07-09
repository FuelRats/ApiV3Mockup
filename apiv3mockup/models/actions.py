from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime)
from sqlalchemy.dialects.postgresql import UUID

from .meta import Base
import datetime
from datetime import timezone

class Actions(Base):
    __tablename__ = 'actions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    inet = Column(String)
    type = Column(String)
    createdAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())