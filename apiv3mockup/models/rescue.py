import enum

from sqlalchemy import (
    Column,
    String,
    GUID,
    JSON,
    Boolean,
    Text,
    Enum,
    ARRAY)

from apiv3mockup.models.rat import Platform
from .meta import Base


class Status(enum.Enum):
    OPEN = 0,
    INACTIVE = 1,
    CLOSED = 2,


class Outcome(enum.Enum):
    SUCCESS = 0,
    FAILURE = 1,
    INVALID = 2,
    OTHER = 3,


class rescue(Base):
    __tablename__ = 'rescues'
    id = Column(GUID, primary_key=True)
    client = Column(String(255))
    codeRed = Column(Boolean)
    data = Column(JSON)
    notes = Column(Text)
    platform = Column(Enum(Platform))
    quotes = Column(ARRAY(JSON))
    status = Column(Enum(Status))
    system = Column(String)
    title = Column(String)
    outcome = Column(Enum(Outcome))
    unidentifiedRats = Column(ARRAY(String))
    firstLimpetId = Column(GUID)
