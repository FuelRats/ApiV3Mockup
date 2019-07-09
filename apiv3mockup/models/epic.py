from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base


class Epic(Base):
    __tablename__ = 'epics'
    id = Column(String, primary_key=True)
    notes = Column(String)
    rescueId = Column(String, ForeignKey('rescues.id'))
    ratId = Column(String, ForeignKey('rats.id'))
    approvedById = Column(String, ForeignKey('users.id'))
    nominatedById = Column(String, ForeignKey('users.id'))
    approvedBy = relationship('User', foreign_keys=[approvedById])
    nominatedBy = relationship('User', foreign_keys=[nominatedById])
    rescue = relationship('Rescue')
    rat = relationship('Rat')
