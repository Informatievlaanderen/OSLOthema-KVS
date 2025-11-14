from enum import Enum


class PubliekeDienstverleningPubliekeDienstverleningFinaliteitId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTFINALITEITTYPEGPMI = "https://data.vlaanderen.be/id/concept/FinaliteitType/GPMI"
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTFINALITEITTYPESOCIAALONDERZOEK = (
        "https://data.vlaanderen.be/id/concept/FinaliteitType/SociaalOnderzoek"
    )

    def __str__(self) -> str:
        return str(self.value)
