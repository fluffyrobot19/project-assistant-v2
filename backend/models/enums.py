from enum import Enum


class AuthLevel(Enum):
    HIGH = "beaver"
    MID = "otter"
    LOW = "duck"


class BudgetType(Enum):
    ACTUAL = "actual"
    TARGET = "target"


class TransactionCode(Enum):
    A = "A"
    B = "B"
    C = "C"


class Currency(Enum):
    HUF = 1
    EUR = 2
    USD = 3
