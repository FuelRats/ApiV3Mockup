from sqlalchemy import (
    Column,
    String,
    GUID,
    ForeignKey
)
from .meta import Base


class Epic(Base):
    __tablename__ = 'epics'
    id = Column(GUID)
    notes = Column(String)
    rescueId = Column(GUID, ForeignKey('rescues.id'))
    ratId = Column(GUID, ForeignKey('rats.id'))
    approvedById = Column(GUID)
    nominatedById = Column(GUID)
