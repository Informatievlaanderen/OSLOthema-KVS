from enum import Enum


class BeroepstoestandBeroepstoestandVoorkeurSKOSPrefLabelValue(str, Enum):
    GEWENST_BEROEP = "Gewenst Beroep"
    TE_LEREN_BEROEP = "Te Leren Beroep"
    TE_VERKENNEN_BEROEP = "Te Verkennen Beroep"
    UITGESLOTEN_BEROEP = "Uitgesloten Beroep"

    def __str__(self) -> str:
        return str(self.value)
