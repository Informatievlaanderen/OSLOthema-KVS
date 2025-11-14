from enum import Enum


class BeroepstoestandBeroepstoestandVoorkeurSKOSPrefLabelLanguage(str, Enum):
    NL = "nl"

    def __str__(self) -> str:
        return str(self.value)
