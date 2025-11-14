from enum import Enum


class JsonLdRootContextItemType1SKOSPrefLabel(str, Enum):
    HTTPWWW_W3_ORG200402SKOSCOREPREFLABEL = "http://www.w3.org/2004/02/skos/core#prefLabel"

    def __str__(self) -> str:
        return str(self.value)
