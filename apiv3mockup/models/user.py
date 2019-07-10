from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    String,
    ARRAY,
    LargeBinary)
from sqlalchemy.dialects.postgresql import JSONB, UUID

from .types.isodatetime import IsoDateTime
from .meta import Base


class User(Base):
    __tablename__ = 'users'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    data = Column(JSONB)
    email = Column(String)
    password = Column(String)
    nicknames = Column(ARRAY(String))
    image = Column(LargeBinary)
    status = Column(String)
    suspended = Column(IsoDateTime)
    permissions = Column(ARRAY(String))
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())
