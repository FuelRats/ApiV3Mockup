from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean, Integer, ARRAY)
from sqlalchemy.dialects.postgresql import UUID
from .types.isodatetime import IsoDateTime

from .meta import Base
import datetime
from datetime import timezone


class Group(Base):
    __tablename__ = 'groups'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    vhost = Column(String)
    isAdministrator = Column(Boolean)
    priority = Column(Integer)
    permissions = Column(ARRAY(String))
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

