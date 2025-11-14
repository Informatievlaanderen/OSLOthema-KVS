from enum import Enum


class ActiveringstrajectActiveringstrajectStatusSKOSPrefLabelValue(str, Enum):
    ACTIEF = "Actief"
    PASSIEF = "Passief"
    STOPGEZET = "Stopgezet"
    UITGEVOERD = "Uitgevoerd"

    def __str__(self) -> str:
        return str(self.value)
