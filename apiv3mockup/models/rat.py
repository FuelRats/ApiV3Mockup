from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4,)
    name = Column(String(255))
    data = Column(JSONB)
    platform = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(DateTime, default=datetime.datetime.now())
    updatedAt = Column(DateTime, onupdate=datetime.datetime.now())
