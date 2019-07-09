from sqlalchemy import (
    Column,
    String,
    GUID)

from .meta import Base


class UserGroups(Base):
    id = Column(GUID)
    groupId = Column(String)
    userId = Column(GUID)
