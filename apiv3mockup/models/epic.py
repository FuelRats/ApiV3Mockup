from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .types.isodatetime import IsoDateTime
from .meta import Base


class Epic(Base):
    __tablename__ = 'epics'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    notes = Column(String)
    rescueId = Column(UUID(as_uuid=True), ForeignKey('rescues.id'))
    ratId = Column(UUID(as_uuid=True), ForeignKey('rats.id'))
    approvedById = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    nominatedById = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    approvedBy = relationship('User', foreign_keys=[approvedById])
    nominatedBy = relationship('User', foreign_keys=[nominatedById])
    rescue = relationship('Rescue')
    rat = relationship('Rat')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

