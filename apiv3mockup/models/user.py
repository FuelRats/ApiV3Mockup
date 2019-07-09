from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    ARRAY,
    DateTime,
    LargeBinary)
from sqlalchemy.dialects.postgresql import JSONB, UUID

from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4,)
    data = Column(JSONB)
    email = Column(String)
    password = Column(String)
    nicknames = Column(ARRAY(String))
    image = Column(LargeBinary)
    status = Column(String)
    suspended = Column(DateTime)
    permissions = Column(ARRAY(String))
