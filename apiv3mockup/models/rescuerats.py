from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .types.isodatetime import IsoDateTime

from .meta import Base
import datetime
from datetime import timezone


class RescueRats(Base):
    __tablename__ = 'rescuerats'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    rescueId = Column(UUID, ForeignKey('rescues.id'))
    ratId = Column(UUID, ForeignKey('rats.id'))
    rescue = relationship('Rescue')
    rat = relationship('Rat')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

