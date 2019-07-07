from sqlalchemy import (
    Column,
    String,
    GUID,
    JSON,
    Enum)
import enum

from .meta import Base


class Platform(enum.Enum):
    PC = 0,
    XB = 1,
    PS = 3,


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(GUID, primary_key=True)
    name = Column(String(255))
    data = Column(JSON)
    platform = Column(Enum(Platform))
    userId = Column(GUID)
