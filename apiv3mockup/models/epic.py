from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from .meta import Base


class Epic(Base):
    __tablename__ = 'epics'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    notes = Column(String)
    rescueId = Column(UUID, ForeignKey('rescues.id'))
    ratId = Column(UUID, ForeignKey('rats.id'))
    approvedById = Column(UUID, ForeignKey('users.id'))
    nominatedById = Column(UUID, ForeignKey('users.id'))
    approvedBy = relationship('User', foreign_keys=[approvedById])
    nominatedBy = relationship('User', foreign_keys=[nominatedById])
    rescue = relationship('Rescue')
    rat = relationship('Rat')
