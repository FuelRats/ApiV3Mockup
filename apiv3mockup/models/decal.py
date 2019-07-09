from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey)


from .meta import Base


class Decal(Base):
    __tablename__ = 'decals'
    id = Column(String, primary_key=True)
    code = Column(String)
    type = Column(String)
    claimedAt = Column(DateTime)
    notes = Column(Text)
    userId = Column(String, ForeignKey('users.id'))
