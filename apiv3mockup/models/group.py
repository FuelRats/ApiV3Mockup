from sqlalchemy import (
    Column,
    String,
    Boolean, Integer, ARRAY)
from .meta import Base


class Group(Base):
    __tablename__ = 'groups'
    id = Column(String, primary_key=True)
    vhost = Column(String)
    isAdministrator = Column(Boolean)
    priority = Column(Integer)
    permissions = Column(ARRAY(String))

