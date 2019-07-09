from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    Boolean,
    Text,
    DateTime,
    ARRAY, ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime


class Rescue(Base):
    __tablename__ = 'rescues'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    client = Column(String(255))
    codeRed = Column(Boolean)
    data = Column(JSONB)
    notes = Column(Text)
    platform = Column(String)
    quotes = Column(ARRAY(JSONB))
    status = Column(String)
    system = Column(String)
    title = Column(String)
    outcome = Column(String)
    unidentifiedRats = Column(ARRAY(String))
    firstLimpetId = Column(UUID, ForeignKey('rats.id'))
    firstLimpet = relationship('Rat')
    createdAt = Column(DateTime, default=datetime.datetime.now())
    updatedAt = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())