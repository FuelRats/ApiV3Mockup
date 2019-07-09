from sqlalchemy import (
    Column,
    String,
    GUID,
    JSON,
    Boolean,
    Text,
    Enum,
    ARRAY, ForeignKey)

from .enums.outcome import Outcome
from .enums.platform import Platform
from .enums.status import Status
from .meta import Base


class Code(Base):
    __tablename__ = 'codes'
    id = Column(GUID, primary_key=True)
    scope = Column(ARRAY)
    value = Column(String)
    redirectUri = Column(String)
    userId = Column(GUID)
    clientId = Column(GUID)
