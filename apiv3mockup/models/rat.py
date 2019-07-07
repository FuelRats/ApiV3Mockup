from sqlalchemy import (
    Column,
    Index,
    String,
    GUID,
    JSON,
    DateTime)

from .meta import Base


class rat(Base):
    __tablename__ = 'rats'
    id = Column(GUID, primary_key=True)
    name = Column(String(255))
    data = Column(JSON)
    joined = Column(DateTime)
    # TODO Absolver: platform enum! platform = Column()
    userId = Column(GUID)


Index('my_index', rat.name, unique=True, mysql_length=255)
