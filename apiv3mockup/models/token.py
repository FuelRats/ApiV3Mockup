from sqlalchemy import (
    Column,
    String,
    ARRAY,
    GUID, ForeignKey)

from .meta import Base


class Token(Base):
    __tablename__ = 'tokens'
    id = Column(GUID)
    scope = Column(ARRAY)
    value = Column(String)
    userId = Column(GUID)
    clientId = Column(GUID)
