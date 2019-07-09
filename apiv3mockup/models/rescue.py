from sqlalchemy import (
    Column,
    String,
    Boolean,
    Text,
    ARRAY, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from .meta import Base

from sqlalchemy.dialects.postgresql import JSONB


class Rescue(Base):
    __tablename__ = 'rescues'
    id = Column(UUID, primary_key=True, default=uuid4,)
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
