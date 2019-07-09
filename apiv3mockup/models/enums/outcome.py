import enum


class Outcome(enum.Enum):
    SUCCESS = 0
    FAILURE = 1
    INVALID = 2
    OTHER = 3