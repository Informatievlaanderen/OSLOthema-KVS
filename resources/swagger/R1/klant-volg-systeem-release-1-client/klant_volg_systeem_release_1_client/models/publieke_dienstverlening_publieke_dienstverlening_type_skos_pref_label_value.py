from enum import Enum


class PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabelValue(str, Enum):
    ACTIVERING_NAAR_WERK = "Activering Naar Werk"

    def __str__(self) -> str:
        return str(self.value)
