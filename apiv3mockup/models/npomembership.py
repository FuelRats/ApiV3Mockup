from sqlalchemy import (
    Column,
    String, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

from .meta import Base


class NPOmembership(Base):
    __tablename__ = 'npomembership'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    userId = Column(String, ForeignKey('users.id'))
    user = relationship('User')
