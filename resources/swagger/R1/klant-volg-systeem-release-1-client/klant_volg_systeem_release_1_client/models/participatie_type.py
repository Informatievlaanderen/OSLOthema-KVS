from enum import Enum


class ParticipatieType(str, Enum):
    PARTICIPATIE = "Participatie"

    def __str__(self) -> str:
        return str(self.value)
