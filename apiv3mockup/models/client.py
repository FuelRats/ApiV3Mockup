from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from .meta import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    name = Column(String)
    secret = Column(String)
    redirectUri = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship("User")
