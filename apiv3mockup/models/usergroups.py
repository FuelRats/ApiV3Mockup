from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from .meta import Base


class UserGroups(Base):
    __tablename__ = 'usergroups'
    id = Column(UUID, primary_key=True, server_default=uuid4, )
    groupId = Column(UUID)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
