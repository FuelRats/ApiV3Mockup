import datetime

from sqlalchemy.types import TypeDecorator, DateTime


class IsoDateTime(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, dialect):
        if value is None:
            return None

        if isinstance(value, datetime.datetime):
            return value.astimezone().isoformat()

        return value

    def process_result_value(self, value, dialect):
        if value is None:
            return None

        return value.astimezone().isoformat()