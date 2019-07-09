import enum


class Status(enum.Enum):
    OPEN = 0,
    INACTIVE = 1,
    CLOSED = 2,


class UserStatus(enum.Enum):
    active = 1,
    inactive = 2,
    legacy = 3,
    deactivated = 4