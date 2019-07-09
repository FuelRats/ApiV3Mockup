from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    Enum,
    ForeignKey)


from .enums.type import Type
from .meta import Base


class Decal(Base):
    __tablename__ = 'decals'
    id = Column(String, primary_key=True)
    code = Column(String)
    type = Column(Enum(Type))
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(String, ForeignKey('users.id'))
