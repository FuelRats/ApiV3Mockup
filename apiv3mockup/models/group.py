from sqlalchemy import (
    Column,
    String,
    Boolean, Integer, ARRAY)
from .meta import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Group(Base):
    __tablename__ = 'groups'
    id = Column(UUID, primary_key=True, default=uuid4,)
    vhost = Column(String)
    isAdministrator = Column(Boolean)
    priority = Column(Integer)
    permissions = Column(ARRAY(String))

