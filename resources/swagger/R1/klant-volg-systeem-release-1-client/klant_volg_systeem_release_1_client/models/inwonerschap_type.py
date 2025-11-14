from enum import Enum


class InwonerschapType(str, Enum):
    INWONERSCHAP = "Inwonerschap"

    def __str__(self) -> str:
        return str(self.value)
