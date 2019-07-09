from sqlalchemy import (
    Column,
    String, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from .meta import Base


class NPOmembership(Base):
    __tablename__ = 'npomembership'
    id = Column(UUID, primary_key=True, default=uuid4,)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
