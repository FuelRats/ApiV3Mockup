from sqlalchemy import (
    Column,
    String,
    JSON,
    ARRAY,
    DateTime,
    Enum, LargeBinary)

from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import text
from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"),)
    data = Column(JSONB)
    email = Column(String)
    password = Column(String)
    nicknames = Column(ARRAY(String))
    image = Column(LargeBinary)
    status = Column(String)
    suspended = Column(DateTime)
    permissions = Column(ARRAY(String))
