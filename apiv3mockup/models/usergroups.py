from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.orm import relationship

from .meta import Base


class UserGroups(Base):
    __tablename__ = 'usergroups'
    id = Column(String, primary_key=True)
    groupId = Column(String)
    userId = Column(String, ForeignKey('users.id'))
    user = relationship('User')