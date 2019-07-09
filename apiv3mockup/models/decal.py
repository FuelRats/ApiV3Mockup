from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from .meta import Base


class Decal(Base):
    __tablename__ = 'decals'
    id = Column(UUID, primary_key=True, default=uuid4,)
    code = Column(String)
    type = Column(String)
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
