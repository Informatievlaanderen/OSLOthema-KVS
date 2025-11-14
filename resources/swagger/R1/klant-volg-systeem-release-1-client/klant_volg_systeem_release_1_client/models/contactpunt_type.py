from enum import Enum


class ContactpuntType(str, Enum):
    CONTACTPUNT = "Contactpunt"

    def __str__(self) -> str:
        return str(self.value)
