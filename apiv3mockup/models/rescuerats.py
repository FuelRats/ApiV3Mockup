from sqlalchemy import (
    Column,
    String, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from .meta import Base


class RescueRats(Base):
    __tablename__ = 'rescuerats'
    id = Column(UUID, primary_key=True, default=uuid4,)
    rescueId = Column(UUID, ForeignKey('rescues.id'))
    ratId = Column(UUID, ForeignKey('rats.id'))
    rescue = relationship('Rescue')
    rat = relationship('Rat')
