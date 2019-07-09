from sqlalchemy import (
    Column,
    String,
    Enum, ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB

from apiv3mockup.models.enums.platform import Platform
from .meta import Base


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(String, primary_key=True)
    name = Column(String(255))
    data = Column(JSONB)
    platform = Column(String)
    userId = Column(String, ForeignKey('users.id'))
