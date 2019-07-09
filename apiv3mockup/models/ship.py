from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    Integer, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base


class Ship(Base):
    __tablename__ = 'ships'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, )
    name = Column(String)
    shipId = Column(Integer)
    shipType = Column(String)
    ratId = Column(UUID, ForeignKey('rats.id'))
    rat = relationship('Rat')
