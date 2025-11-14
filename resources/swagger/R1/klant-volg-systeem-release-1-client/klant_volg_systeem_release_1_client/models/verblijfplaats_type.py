from enum import Enum


class VerblijfplaatsType(str, Enum):
    VERBLIJFPLAATS = "Verblijfplaats"

    def __str__(self) -> str:
        return str(self.value)
