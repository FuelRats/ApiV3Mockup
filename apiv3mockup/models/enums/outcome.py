import enum


class Outcome(enum.Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'
    INVALID = 'invalid'
    OTHER = 'other'