from sqlalchemy import (
    Column,
    Index,
    String,
    GUID,
    JSON,
    Enum,
    DateTime)
import enum

from .meta import Base


class Platform(enum.Enum):
    PS = 1,
    PC = 2,
    XB = 3,


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(GUID, primary_key=True)
    name = Column(String(255))
    data = Column(JSON)
    joined = Column(DateTime)
    platform = Column(Enum(Platform))
    # TODO Absolver: platform enum! platform = Column()
    userId = Column(GUID)


Index('my_index', rat.name, unique=True, mysql_length=255)
