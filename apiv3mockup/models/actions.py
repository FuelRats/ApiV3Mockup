from sqlalchemy import (
    Column,
    String)


from .meta import Base


class Actions(Base):
    __tablename__ = 'actions'
    id = Column(String, primary_key=True)
    inet = Column(String)
    type = Column(String)
