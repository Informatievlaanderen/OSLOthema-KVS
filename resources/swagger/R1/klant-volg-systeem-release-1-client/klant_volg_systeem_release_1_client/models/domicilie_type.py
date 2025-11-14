from enum import Enum


class DomicilieType(str, Enum):
    DOMICILIE = "Domicilie"

    def __str__(self) -> str:
        return str(self.value)
