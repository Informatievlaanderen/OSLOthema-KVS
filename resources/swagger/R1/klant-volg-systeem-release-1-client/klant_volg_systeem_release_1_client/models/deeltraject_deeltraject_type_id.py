from enum import Enum


class DeeltrajectDeeltrajectTypeId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTDEELTRAJECTTYPEOPLEIDING = (
        "https://data.vlaanderen.be/id/concept/Deeltrajecttype/Opleiding"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTDEELTRAJECTTYPEORIENTERING = (
        "https://data.vlaanderen.be/id/concept/Deeltrajecttype/Orientering"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTDEELTRAJECTTYPETENDER = (
        "https://data.vlaanderen.be/id/concept/Deeltrajecttype/Tender"
    )

    def __str__(self) -> str:
        return str(self.value)
