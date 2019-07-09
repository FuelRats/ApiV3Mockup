from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

from .meta import Base


class Decal(Base):
    __tablename__ = 'decals'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    code = Column(String)
    type = Column(String)
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship('User')
