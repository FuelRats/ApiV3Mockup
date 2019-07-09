from sqlalchemy import (
    Column,
    String,
    GUID)

from .meta import Base


class Actions(Base):
    __tablename__ = 'actions'
    id = Column(GUID)
    inet = Column(String)
    type = Column(String)
