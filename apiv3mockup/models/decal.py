from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    String,
    Text,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .types.isodatetime import IsoDateTime
from .meta import Base


class Decal(Base):
    """
    Provides decal codes for redeeming the Fuel Rats decal from the Frontier Store.
    """
    __tablename__ = 'decals'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    code = Column(String)
    type = Column(String)
    claimedAt = Column(IsoDateTime)
    notes = Column(Text)
    userId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(),
                       onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

