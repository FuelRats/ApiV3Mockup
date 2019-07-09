import enum


class UserStatus(enum.Enum):
    active = 1,
    inactive = 2,
    legacy = 3,
    deactivated = 4
