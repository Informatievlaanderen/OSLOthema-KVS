from enum import Enum


class PersoonType(str, Enum):
    PERSOON = "Persoon"

    def __str__(self) -> str:
        return str(self.value)
