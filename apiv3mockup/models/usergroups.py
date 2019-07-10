from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .types.isodatetime import IsoDateTime
from .meta import Base


class UserGroups(Base):
    __tablename__ = 'usergroups'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, )
    groupId = Column(UUID(as_uuid=True))
    userId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(),
                       onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())
