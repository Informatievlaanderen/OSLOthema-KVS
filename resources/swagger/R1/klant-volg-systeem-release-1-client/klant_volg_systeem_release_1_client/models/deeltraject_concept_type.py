from enum import Enum


class DeeltrajectConceptType(str, Enum):
    SKOSCONCEPT = "SKOS:Concept"
    SKOSCONCEPTSCHEME = "SKOS:ConceptScheme"

    def __str__(self) -> str:
        return str(self.value)
