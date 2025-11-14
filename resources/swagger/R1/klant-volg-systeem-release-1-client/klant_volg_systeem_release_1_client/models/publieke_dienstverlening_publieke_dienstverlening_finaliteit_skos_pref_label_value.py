from enum import Enum


class PubliekeDienstverleningPubliekeDienstverleningFinaliteitSKOSPrefLabelValue(str, Enum):
    GPMI = "GPMI"
    SOCIAAL_ONDERZOEK = "Sociaal Onderzoek"

    def __str__(self) -> str:
        return str(self.value)
