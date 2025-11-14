from enum import Enum


class PubliekeOrganisatieType(str, Enum):
    PUBLIEKEORGANISATIE = "PubliekeOrganisatie"

    def __str__(self) -> str:
        return str(self.value)
