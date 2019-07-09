from uuid import uuid4

from sqlalchemy import (
    Column,
    ForeignKey,
    DateTime)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime


class NPOmembership(Base):
    __tablename__ = 'npomembership'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(DateTime, default=datetime.datetime.now())
    updatedAt = Column(DateTime, onupdate=datetime.datetime.now())
