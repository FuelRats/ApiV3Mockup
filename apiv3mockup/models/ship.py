from sqlalchemy import (
    Column,
    String,
    GUID, Integer, Enum, ForeignKey)
from .meta import Base
from .enums.shiptypes import ShipTypes


class Client(Base):
    id = Column(GUID)
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(Enum(ShipTypes))
    ratId = Column(GUID, ForeignKey('rats.id'))
