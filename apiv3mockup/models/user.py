from sqlalchemy import (
    Column,
    String,
    JSON,
    BLOB,
    ARRAY,
    DateTime,
    Enum)

from .meta import Base
from .enums.status import UserStatus


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
