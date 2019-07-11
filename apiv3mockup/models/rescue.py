from uuid import uuid4
from datetime import timezone
import datetime

from sqlalchemy import (
    Column,
    String,
    Boolean,
    Text,
    ARRAY,
    ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .types.isodatetime import IsoDateTime
from .meta import Base
from sqlalchemy import Table

Rescue_Rats = Table('rescuerats', Base.metadata,
                    Column('rescueId', UUID(as_uuid=True), ForeignKey('rescues.id')),
                    Column('ratId', UUID(as_uuid=True), ForeignKey('rats.id')))


class Rescue(Base):
    __tablename__ = 'rescues'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    client = Column(String(255))
    codeRed = Column(Boolean)
    data = Column(JSONB)
    notes = Column(Text)
    platform = Column(String)
    quotes = Column(JSONB)
    status = Column(String)
    system = Column(String)
    title = Column(String)
    outcome = Column(String)
    unidentifiedRats = Column(ARRAY(String))
    firstLimpetId = Column(UUID(as_uuid=True), ForeignKey('rats.id'))
    firstLimpet = relationship('Rat')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(),
                       onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    rats = relationship('Rat', secondary=Rescue_Rats)
