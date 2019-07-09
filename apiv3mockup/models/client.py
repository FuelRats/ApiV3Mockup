from sqlalchemy import (
    Column,
    String,
    GUID)
from .meta import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(GUID, primary_key=True)
    name = Column(String)
    secret = Column(String)
    redirectUri = Column(String)
    userId = Column(String)
