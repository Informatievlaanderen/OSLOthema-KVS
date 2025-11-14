from enum import Enum


class DeeltrajectDeeltrajectStatusSKOSPrefLabelValue(str, Enum):
    ACTIEF = "Actief"
    PASSIEF = "Passief"
    STOPGEZET = "Stopgezet"
    UITGEVOERD = "Uitgevoerd"

    def __str__(self) -> str:
        return str(self.value)
