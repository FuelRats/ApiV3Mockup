from sqlalchemy import (
    Column,
    String,
    Boolean,
    Text,
    ARRAY, ForeignKey)

from .meta import Base

from sqlalchemy.dialects.postgresql import JSONB


class Rescue(Base):
    __tablename__ = 'rescues'
    id = Column(String, primary_key=True)
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
    firstLimpetId = Column(String, ForeignKey('rats.id'))
