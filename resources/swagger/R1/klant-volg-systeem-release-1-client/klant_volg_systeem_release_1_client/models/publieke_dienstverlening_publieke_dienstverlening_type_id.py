from enum import Enum


class PubliekeDienstverleningPubliekeDienstverleningTypeId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTPUBLIEKEDIENSTVERLENINGTYPEACTIVERINGNAARWERK = (
        "https://data.vlaanderen.be/id/concept/PubliekeDienstverleningType/ActiveringNaarWerk"
    )

    def __str__(self) -> str:
        return str(self.value)
