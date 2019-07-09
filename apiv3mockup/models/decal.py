from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime


class Decal(Base):
    __tablename__ = 'decals'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    code = Column(String)
    type = Column(String)
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
    createdAt = Column(DateTime, default=datetime.datetime.now())
    updatedAt = Column(DateTime, onupdate=datetime.datetime.now())
