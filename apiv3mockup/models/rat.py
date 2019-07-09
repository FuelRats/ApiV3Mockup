from sqlalchemy import (
    Column,
    String,
    JSON,
    Enum, ForeignKey)

from apiv3mockup.models.enums.platform import Platform
from .meta import Base


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(String, primary_key=True)
    name = Column(String(255))
    data = Column(JSON)
    platform = Column(Enum(Platform))
    userId = Column(String, ForeignKey('users.id'))
