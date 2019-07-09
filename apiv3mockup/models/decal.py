from sqlalchemy import (
    Column,
    String,
    GUID,
    DateTime,
    Text,
    Enum
)


from .enums.type import Type
from .meta import Base


class Decal(Base):
    __tablename__ = 'decals'
    id = Column(GUID)
    code = Column(String)
    type = Column(Enum(Type))
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(GUID)
