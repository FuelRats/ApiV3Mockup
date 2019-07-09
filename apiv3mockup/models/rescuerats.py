from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime


class RescueRats(Base):
    __tablename__ = 'rescuerats'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    rescueId = Column(UUID, ForeignKey('rescues.id'))
    ratId = Column(UUID, ForeignKey('rats.id'))
    rescue = relationship('Rescue')
    rat = relationship('Rat')
    createdAt = Column(DateTime, default=datetime.datetime.now())
    updatedAt = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())