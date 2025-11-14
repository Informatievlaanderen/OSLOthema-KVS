from enum import Enum


class ActiveringstrajectActiveringstrajectStatusId(str, Enum):
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTTRAJECTSTATUSACTIEF = "https://data.vlaanderen.be/id/concept/TrajectStatus/Actief"
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTTRAJECTSTATUSPASSIEF = "https://data.vlaanderen.be/id/concept/TrajectStatus/Passief"
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTTRAJECTSTATUSSTOPGEZET = (
        "https://data.vlaanderen.be/id/concept/TrajectStatus/Stopgezet"
    )
    HTTPSDATA_VLAANDEREN_BEIDCONCEPTTRAJECTSTATUSUITGEVOERD = (
        "https://data.vlaanderen.be/id/concept/TrajectStatus/Uitgevoerd"
    )

    def __str__(self) -> str:
        return str(self.value)
