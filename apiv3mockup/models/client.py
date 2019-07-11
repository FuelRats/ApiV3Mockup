from uuid import uuid4
import datetime
from datetime import timezone

from sqlalchemy import (
    Column,
    String,
    ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .types.isodatetime import IsoDateTime
from .meta import Base


class Client(Base):
    """
    Represents a third party API client in the database.

    All the parameters are there, but Swagger doesn't care. :(
    """
    __tablename__ = 'clients'
    __json_exclude__ = {"createdAt", "updatedAt"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, doc='Primary key')
    name = Column(String, doc='Client name. An arbitrary string for human readability.')
    secret = Column(String, doc='The client secret. Must be kept... secret.')
    redirectUri = Column(String, doc='Redirect URI for the client\'s oauth process')
    userId = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("User")
    createdAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat())
    updatedAt = Column(IsoDateTime, default=datetime.datetime.now(timezone.utc).astimezone().isoformat(),
                       onupdate=datetime.datetime.now(timezone.utc).astimezone().isoformat())

