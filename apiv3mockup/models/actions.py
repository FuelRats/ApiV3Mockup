from uuid import uuid4

from sqlalchemy import (
    Column,
    String)
from sqlalchemy.dialects.postgresql import UUID

from .meta import Base


class Actions(Base):
    __tablename__ = 'actions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    inet = Column(String)
    type = Column(String)
