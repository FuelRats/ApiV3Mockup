from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .types.isodatetime import IsoDateTime

from .meta import Base
import datetime
from datetime import timezone


class Decal(Base):
    __tablename__ = 'decals'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    code = Column(String)
    type = Column(String)
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

