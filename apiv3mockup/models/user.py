from sqlalchemy import (
    Column,
    String,
    JSON,
    BLOB,
    ARRAY,
    DateTime,
    GUID,
    Enum)

from apiv3mockup.models.enums.userStatus import UserStatus
from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(GUID)
    data = Column(JSON)
    email = Column(String)
    password = Column(String)
    nicknames = Column(ARRAY)
    image = Column(BLOB)
    status = Column(Enum(UserStatus))
    suspended = Column(DateTime)
    permissions = Column(ARRAY)
