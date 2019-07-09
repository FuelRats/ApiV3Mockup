from sqlalchemy import (
    Column,
    String,
    JSON,
    Boolean,
    Text,
    Enum,
    ARRAY, ForeignKey)

from .enums.outcome import Outcome
from .enums.platform import Platform
from .enums.status import Status
from .meta import Base

from sqlalchemy.dialects.postgresql import JSONB


class Rescue(Base):
    __tablename__ = 'rescues'
    id = Column(String, primary_key=True)
    client = Column(String(255))
    codeRed = Column(Boolean)
    data = Column(JSONB)
    notes = Column(Text)
    platform = Column(Enum(Platform))
    quotes = Column(ARRAY(JSONB))
    status = Column(Enum(Status))
    system = Column(String)
    title = Column(String)
    outcome = Column(Enum(Outcome))
    unidentifiedRats = Column(ARRAY(String))
    firstLimpetId = Column(String, ForeignKey('rats.id'))
