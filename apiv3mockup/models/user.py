from sqlalchemy import (
    Column,
    String,
    JSON,
    ARRAY,
    DateTime,
    Enum, LargeBinary)

from sqlalchemy.dialects.postgresql import JSONB

from apiv3mockup.models.enums.userStatus import UserStatus
from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    data = Column(JSONB)
    email = Column(String)
    password = Column(String)
    nicknames = Column(ARRAY(String))
    image = Column(LargeBinary)
    status = Column(String)
    suspended = Column(DateTime)
    permissions = Column(ARRAY(String))
