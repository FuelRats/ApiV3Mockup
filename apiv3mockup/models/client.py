from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.orm import relationship

from .meta import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(String, primary_key=True)
    name = Column(String)
    secret = Column(String)
    redirectUri = Column(String)
    userId = Column(String, ForeignKey('users.id'))
    user = relationship("User")