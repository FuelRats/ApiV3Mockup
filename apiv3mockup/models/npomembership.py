from sqlalchemy import (
    Column,
    String, ForeignKey)
from .meta import Base


class NPOmembership(Base):
    __tablename__ = 'npomembership'
    id = Column(String, primary_key=True)
    userId = Column(String, ForeignKey('users.id'))
