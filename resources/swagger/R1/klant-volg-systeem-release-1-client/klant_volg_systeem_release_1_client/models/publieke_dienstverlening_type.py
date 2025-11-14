from enum import Enum


class PubliekeDienstverleningType(str, Enum):
    PUBLIEKEDIENSTVERLENING = "PubliekeDienstverlening"

    def __str__(self) -> str:
        return str(self.value)
