from uuid import uuid4

from sqlalchemy import (
    Column,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base


class NPOmembership(Base):
    __tablename__ = 'npomembership'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
