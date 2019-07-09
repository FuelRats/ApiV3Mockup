from sqlalchemy import (
    Column,
    String,
    GUID,
    JSON,
    Boolean,
    Text,
    Enum,
    ARRAY, ForeignKey)

from .enums.outcome import Outcome
from .enums.platform import Platform
from .enums.status import Status
from .meta import Base


class Rescue(Base):
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
    firstLimpetId = Column(GUID, ForeignKey('rats.id'))
