from enum import Enum


class IdentificatorType(str, Enum):
    IDENTIFICATOR = "Identificator"

    def __str__(self) -> str:
        return str(self.value)
