from enum import Enum


class DeeltrajectDeeltrajectNaamLanguage(str, Enum):
    NL = "nl"

    def __str__(self) -> str:
        return str(self.value)
