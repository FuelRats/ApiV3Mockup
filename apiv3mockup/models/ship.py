from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime
from datetime import timezone

class Ship(Base):
    __tablename__ = 'ships'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, )
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(String)
    ratId = Column(UUID, ForeignKey('rats.id'))
    rat = relationship('Rat')
    createdAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())