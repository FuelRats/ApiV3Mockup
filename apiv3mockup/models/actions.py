from sqlalchemy import (
    Column,
    String)


from .meta import Base

from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Actions(Base):
    __tablename__ = 'actions'
    id = Column(UUID, primary_key=True, default=uuid4,)
    inet = Column(String)
    type = Column(String)
