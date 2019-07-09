from uuid import uuid4

from sqlalchemy import (
    Column,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base


class UserGroups(Base):
    __tablename__ = 'usergroups'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, )
    groupId = Column(UUID)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
