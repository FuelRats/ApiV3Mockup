from sqlalchemy import (
    Column,
    String,
    JSON,
    BLOB,
    ARRAY,
    DateTime,
    Enum)

from apiv3mockup.models.enums.userStatus import UserStatus
from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    data = Column(JSON)
    email = Column(String)
    password = Column(String)
    nicknames = Column(ARRAY(String))
    image = Column(BLOB)
    status = Column(Enum(UserStatus))
    suspended = Column(DateTime)
    permissions = Column(ARRAY(String))
