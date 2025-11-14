from enum import Enum


class ParticipatieParticipatieRolId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTPARTICIPATIETYPEBEGELEIDER = (
        "https://data.vlaanderen.be/id/concept/Participatietype/Begeleider"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTPARTICIPATIETYPEBEMIDDELAAR = (
        "https://data.vlaanderen.be/id/concept/Participatietype/Bemiddelaar"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTPARTICIPATIETYPECONTACTPERSOON = (
        "https://data.vlaanderen.be/id/concept/Participatietype/Contactpersoon"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTPARTICIPATIETYPEWERKZOEKENDE = (
        "https://data.vlaanderen.be/id/concept/Participatietype/Werkzoekende"
    )

    def __str__(self) -> str:
        return str(self.value)
