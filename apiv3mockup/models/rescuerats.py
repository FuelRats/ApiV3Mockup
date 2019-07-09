from sqlalchemy import (
    Column,
    String,
    GUID)
from .meta import Base


class RescueRats(Base):
    __tablename__ = 'rescuerats'
    id = Column(GUID)
    rescueId = Column(GUID)
    ratId = Column(GUID)
