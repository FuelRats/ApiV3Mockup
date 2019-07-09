from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB

from .meta import Base


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(String, primary_key=True)
    name = Column(String(255))
    data = Column(JSONB)
    platform = Column(String)
    userId = Column(String, ForeignKey('users.id'))
