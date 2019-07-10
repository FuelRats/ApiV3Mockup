from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    String,
    Integer, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .types.isodatetime import IsoDateTime
from .meta import Base


class Ship(Base):
    __tablename__ = 'ships'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, )
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(String)
    ratId = Column(UUID(as_uuid=True), ForeignKey('rats.id'))
    rat = relationship('Rat')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(),
                       onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

