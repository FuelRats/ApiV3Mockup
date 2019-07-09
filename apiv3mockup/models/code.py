from sqlalchemy import (
    Column,
    String,
    ARRAY, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

from .meta import Base


class Code(Base):
    __tablename__ = 'codes'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    scope = Column(ARRAY(String))
    value = Column(String)
    redirectUri = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    clientId = Column(UUID, ForeignKey('clients.id'))
    user = relationship('User')
    client = relationship('Client')
