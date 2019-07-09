from sqlalchemy import (
    Column,
    String,
    GUID,
    Boolean, Integer, ARRAY)
from .meta import Base


class Group(Base):
    __tablename__ = 'groups'
    id = Column(GUID)
    vhost = Column(String)
    isAdministrator = Column(Boolean)
    priority = Column(Integer)
    permissions = Column(ARRAY)

