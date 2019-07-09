from sqlalchemy import (
    Column,
    String, ForeignKey)
from sqlalchemy.orm import relationship

from .meta import Base


class RescueRats(Base):
    __tablename__ = 'rescuerats'
    id = Column(String, primary_key=True)
    rescueId = Column(String, ForeignKey('rescues.id'))
    ratId = Column(String, ForeignKey('rats.id'))
    rescue = relationship('Rescue')
    rat = relationship('Rat')
