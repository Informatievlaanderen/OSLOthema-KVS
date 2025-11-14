from enum import Enum


class GeregistreerdeOrganisatieType(str, Enum):
    GEREGISTREERDEORGANISATIE = "GeregistreerdeOrganisatie"

    def __str__(self) -> str:
        return str(self.value)
