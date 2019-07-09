from sqlalchemy import (
    Column,
    String,
    GUID,
    ARRAY)

from .meta import Base


class Code(Base):
    __tablename__ = 'codes'
    id = Column(GUID, primary_key=True)
    scope = Column(ARRAY)
    value = Column(String)
    redirectUri = Column(String)
    userId = Column(GUID)
    clientId = Column(GUID)
