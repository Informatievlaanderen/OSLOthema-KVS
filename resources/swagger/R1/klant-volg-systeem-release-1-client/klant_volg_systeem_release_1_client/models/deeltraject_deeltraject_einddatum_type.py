from enum import Enum


class DeeltrajectDeeltrajectEinddatumType(str, Enum):
    DATETIME = "DateTime"

    def __str__(self) -> str:
        return str(self.value)
