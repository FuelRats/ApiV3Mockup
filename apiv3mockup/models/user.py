from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    ARRAY,
    DateTime,
    LargeBinary)
from sqlalchemy.dialects.postgresql import JSONB, UUID

from .meta import Base
import datetime
from datetime import timezone


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
    suspended = Column(DateTime)
    permissions = Column(ARRAY(String))
    createdAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())