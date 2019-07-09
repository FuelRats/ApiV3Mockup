from sqlalchemy import (
    Column,
    String,
    GUID)
from .meta import Base


class NPOmembership(Base):
    __tablename__ = 'npomembership'
    id = Column(GUID)
    userId = Column(GUID)
