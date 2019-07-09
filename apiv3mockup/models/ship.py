from sqlalchemy import (
    Column,
    String,
    Integer, ForeignKey)
from sqlalchemy.orm import relationship

from .meta import Base



class Ship(Base):
    __tablename__ = 'ships'
    id = Column(String, primary_key=True)
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(String)
    ratId = Column(String, ForeignKey('rats.id'))
    rat = relationship('Rat')
