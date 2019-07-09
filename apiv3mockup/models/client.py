from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from .meta import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(UUID, primary_key=True, default=uuid4,)
    name = Column(String)
    secret = Column(String)
    redirectUri = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship("User")
