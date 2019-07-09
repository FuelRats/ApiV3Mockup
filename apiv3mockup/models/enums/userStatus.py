import enum


class UserStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'
    legacy = 'legacy'
    deactivated = 'deactivated'
