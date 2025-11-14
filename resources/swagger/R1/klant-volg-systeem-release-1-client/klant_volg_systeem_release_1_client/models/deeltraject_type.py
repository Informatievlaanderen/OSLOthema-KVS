from enum import Enum


class DeeltrajectType(str, Enum):
    DEELTRAJECT = "Deeltraject"

    def __str__(self) -> str:
        return str(self.value)
