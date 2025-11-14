from enum import Enum


class WerkvoorkeurenType(str, Enum):
    WERKVOORKEUREN = "Werkvoorkeuren"

    def __str__(self) -> str:
        return str(self.value)
