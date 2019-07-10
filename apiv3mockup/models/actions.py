from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    String)
from sqlalchemy.dialects.postgresql import UUID

from .meta import Base
from .types.isodatetime import IsoDateTime


class Actions(Base):
    __tablename__ = 'actions'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    inet = Column(String)
    type = Column(String)
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(),
                       onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

