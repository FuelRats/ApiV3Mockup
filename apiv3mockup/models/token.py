from sqlalchemy import (
    Column,
    String,
    ARRAY,
    ForeignKey)

from .meta import Base


class Token(Base):
    __tablename__ = 'tokens'
    id = Column(String, primary_key=True)
    scope = Column(ARRAY(String))
    value = Column(String)
    userId = Column(String, ForeignKey('users.id'))
    clientId = Column(String, ForeignKey('clients.id'))
