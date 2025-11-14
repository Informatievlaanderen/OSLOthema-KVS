from enum import Enum


class AdresvoorstellingType(str, Enum):
    ADRESVOORSTELLING = "Adresvoorstelling"

    def __str__(self) -> str:
        return str(self.value)
