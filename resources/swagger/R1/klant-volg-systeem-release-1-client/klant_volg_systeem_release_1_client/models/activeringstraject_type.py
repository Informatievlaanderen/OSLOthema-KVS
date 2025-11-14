from enum import Enum


class ActiveringstrajectType(str, Enum):
    ACTIVERINGSTRAJECT = "Activeringstraject"

    def __str__(self) -> str:
        return str(self.value)
