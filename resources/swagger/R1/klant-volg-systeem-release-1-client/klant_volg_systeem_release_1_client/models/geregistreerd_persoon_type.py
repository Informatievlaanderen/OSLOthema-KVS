from enum import Enum


class GeregistreerdPersoonType(str, Enum):
    GEREGISTREERDPERSOON = "GeregistreerdPersoon"

    def __str__(self) -> str:
        return str(self.value)
