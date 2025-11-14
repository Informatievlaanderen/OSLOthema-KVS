from enum import Enum


class PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabelLanguage(str, Enum):
    NL = "nl"

    def __str__(self) -> str:
        return str(self.value)
