from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime
from datetime import timezone

class UserGroups(Base):
    __tablename__ = 'usergroups'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, )
    groupId = Column(UUID)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(DateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(), onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())
