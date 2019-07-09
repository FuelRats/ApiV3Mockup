from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import text
from sqlalchemy.orm import relationship

from .meta import Base


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    name = Column(String(255))
    data = Column(JSONB)
    platform = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
