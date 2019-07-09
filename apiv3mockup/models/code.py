from sqlalchemy import (
    Column,
    String,
    ARRAY, ForeignKey)

from .meta import Base


class Code(Base):
    __tablename__ = 'codes'
    id = Column(String, primary_key=True)
    scope = Column(ARRAY(String))
    value = Column(String)
    redirectUri = Column(String)
    userId = Column(String, ForeignKey('users.id'))
    clientId = Column(String, ForeignKey('clients.id'))
