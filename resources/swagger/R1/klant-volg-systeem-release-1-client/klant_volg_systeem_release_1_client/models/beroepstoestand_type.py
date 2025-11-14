from enum import Enum


class BeroepstoestandType(str, Enum):
    BEROEPSTOESTAND = "Beroepstoestand"

    def __str__(self) -> str:
        return str(self.value)
