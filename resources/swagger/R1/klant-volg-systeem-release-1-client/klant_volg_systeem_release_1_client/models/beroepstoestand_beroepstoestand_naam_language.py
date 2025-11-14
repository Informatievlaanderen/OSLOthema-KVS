from enum import Enum


class BeroepstoestandBeroepstoestandNaamLanguage(str, Enum):
    NL = "nl"

    def __str__(self) -> str:
        return str(self.value)
