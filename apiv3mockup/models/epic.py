from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from .meta import Base


class Epic(Base):
    __tablename__ = 'epics'
    id = Column(String, primary_key=True)
    notes = Column(String)
    rescueId = Column(String, ForeignKey('rescues.id'))
    ratId = Column(String, ForeignKey('rats.id'))
    approvedById = Column(String, ForeignKey('users.id'))
    nominatedById = Column(String, ForeignKey('users.id'))
