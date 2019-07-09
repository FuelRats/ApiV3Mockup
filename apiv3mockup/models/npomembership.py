from uuid import uuid4

from sqlalchemy import (
    Column,
    ForeignKey,
    DateTime)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime
from datetime import timezone

class NPOmembership(Base):
    __tablename__ = 'npomembership'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())