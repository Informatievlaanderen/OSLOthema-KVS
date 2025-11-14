from enum import Enum


class GeregistreerdeOrganisatieGeregistreerdeOrganisatieTypeSKOSPrefLabelValue(str, Enum):
    OCMW = "OCMW"
    VDAB = "VDAB"

    def __str__(self) -> str:
        return str(self.value)
