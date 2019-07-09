from sqlalchemy import (
    Column,
    String,
    Integer, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from .meta import Base


class Ship(Base):
    __tablename__ = 'ships'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"), )
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(String)
    ratId = Column(UUID, ForeignKey('rats.id'))
    rat = relationship('Rat')
