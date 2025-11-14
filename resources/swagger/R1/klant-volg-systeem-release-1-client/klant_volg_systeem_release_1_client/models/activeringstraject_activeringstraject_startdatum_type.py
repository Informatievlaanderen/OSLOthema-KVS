from enum import Enum


class ActiveringstrajectActiveringstrajectStartdatumType(str, Enum):
    DATETIME = "DateTime"

    def __str__(self) -> str:
        return str(self.value)
