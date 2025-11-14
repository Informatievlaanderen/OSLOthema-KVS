from enum import Enum


class ParticipatieParticipatieRolSKOSPrefLabelValue(str, Enum):
    BEGELEIDER = "Begeleider"
    BEMIDDELAAR = "Bemiddelaar"
    CONTACTPERSOON = "Contactpersoon"
    WERKZOEKENDE = "Werkzoekende"

    def __str__(self) -> str:
        return str(self.value)
