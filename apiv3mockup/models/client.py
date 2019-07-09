from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base
import datetime


class Client(Base):
    __tablename__ = 'clients'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    name = Column(String)
    secret = Column(String)
    redirectUri = Column(String)
    userId = Column(UUID, ForeignKey('users.id'))
    user = relationship("User")
    createdAt = Column(DateTime, default=datetime.datetime.now())
    updatedAt = Column(DateTime, onupdate=datetime.datetime.now())
