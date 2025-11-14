from enum import Enum


class BeroepstoestandBeroepstoestandVoorkeurId(str, Enum):
    HTTPDATA_VLAANDEREN_BEIDCONCEPTVOORKEURTYPEGEWENSTBEROEP = (
        "http://data.vlaanderen.be/id/concept/Voorkeurtype/GewenstBeroep"
    )
    HTTPDATA_VLAANDEREN_BEIDCONCEPTVOORKEURTYPETELERENBEROEP = (
        "http://data.vlaanderen.be/id/concept/Voorkeurtype/TeLerenBeroep"
    )
    HTTPDATA_VLAANDEREN_BEIDCONCEPTVOORKEURTYPETEVERKENNENBEROEP = (
        "http://data.vlaanderen.be/id/concept/Voorkeurtype/TeVerkennenBeroep"
    )
    HTTPDATA_VLAANDEREN_BEIDCONCEPTVOORKEURTYPEUITGESLOTENBEROEP = (
        "http://data.vlaanderen.be/id/concept/Voorkeurtype/UitgeslotenBeroep"
    )

    def __str__(self) -> str:
        return str(self.value)
