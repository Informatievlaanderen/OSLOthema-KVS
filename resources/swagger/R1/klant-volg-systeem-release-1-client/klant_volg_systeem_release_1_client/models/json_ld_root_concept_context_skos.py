from enum import Enum


class JsonLdRootConceptContextSKOS(str, Enum):
    HTTPWWW_W3_ORG200402SKOSCORE = "http://www.w3.org/2004/02/skos/core#"

    def __str__(self) -> str:
        return str(self.value)
