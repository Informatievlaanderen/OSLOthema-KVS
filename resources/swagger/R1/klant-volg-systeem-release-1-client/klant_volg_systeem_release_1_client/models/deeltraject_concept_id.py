from enum import Enum


class DeeltrajectConceptId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTDEELTRAJECTTYPEOPLEIDING = (
        "https://data.vlaanderen.be/id/concept/Deeltrajecttype/Opleiding"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTDEELTRAJECTTYPEORIENTERING = (
        "https://data.vlaanderen.be/id/concept/Deeltrajecttype/Orientering"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTDEELTRAJECTTYPETENDER = (
        "https://data.vlaanderen.be/id/concept/Deeltrajecttype/Tender"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTSCHEMEDEELTRAJECTTYPE = (
        "https://data.vlaanderen.be/id/conceptscheme/Deeltrajecttype"
    )

    def __str__(self) -> str:
        return str(self.value)
