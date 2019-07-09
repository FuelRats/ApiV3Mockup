from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    ARRAY,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base


class Token(Base):
    __tablename__ = 'tokens'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    scope = Column(ARRAY(String))
    value = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    clientId = Column(UUID, ForeignKey('clients.id'))
    user = relationship('User')
    client = relationship('Client')
