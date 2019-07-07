from sqlalchemy import (
    Column,
    String,
    GUID,
    JSON,
    Enum)

from apiv3mockup.models.enums.platform import Platform
from .meta import Base


class Rat(Base):
    __tablename__ = 'rats'
    id = Column(GUID, primary_key=True)
    name = Column(String(255))
    data = Column(JSON)
    platform = Column(Enum(Platform))
    userId = Column(GUID)
