from enum import Enum


class PubliekeOrganisatiePubliekeOrganisatieTypeId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTORGANISATIETYPEOCMW = "https://data.vlaanderen.be/id/concept/OrganisatieType/OCMW"
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTORGANISATIETYPEVDAB = "https://data.vlaanderen.be/id/concept/OrganisatieType/VDAB"

    def __str__(self) -> str:
        return str(self.value)
