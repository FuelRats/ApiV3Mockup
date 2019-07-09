from sqlalchemy import (
    Column,
    String,
    Integer, Enum, ForeignKey)
from .meta import Base
from .enums.shiptypes import ShipTypes


class Ship(Base):
    __tablename__ = 'ships'
    id = Column(String, primary_key=True)
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(Enum(ShipTypes))
    ratId = Column(String, ForeignKey('rats.id'))
