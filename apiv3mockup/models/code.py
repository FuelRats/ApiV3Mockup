from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ARRAY, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .types.isodatetime import IsoDateTime

from .meta import Base
import datetime
from datetime import timezone


class Code(Base):
    __tablename__ = 'codes'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    scope = Column(ARRAY(String))
    value = Column(String)
    redirectUri = Column(String)
    userId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    clientId = Column(UUID(as_uuid=True), ForeignKey('clients.id'))
    user = relationship('User')
    client = relationship('Client')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

