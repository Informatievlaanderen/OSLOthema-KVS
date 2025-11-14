from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deeltraject_concept_id import DeeltrajectConceptId
from ..models.deeltraject_concept_type import DeeltrajectConceptType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deeltraject_concept_skos_definition import DeeltrajectConceptSKOSDefinition
    from ..models.deeltraject_concept_skos_inscheme import DeeltrajectConceptSKOSInscheme
    from ..models.deeltraject_concept_skos_pref_label import DeeltrajectConceptSKOSPrefLabel
    from ..models.deeltraject_concept_skos_top_concept_of import DeeltrajectConceptSKOSTopConceptOf


T = TypeVar("T", bound="DeeltrajectConcept")


@_attrs_define
class DeeltrajectConcept:
    """Deeltraject soort

    Attributes:
        id (DeeltrajectConceptId): URI dat het Concept uniek refereert.
        type_ (DeeltrajectConceptType): Object type.
        skos_pref_label (DeeltrajectConceptSKOSPrefLabel): Label van het concept.
        skos_definition (DeeltrajectConceptSKOSDefinition): Definitie van het concept.
        skos_inscheme (DeeltrajectConceptSKOSInscheme | Unset): Verwijzing naar waar het Concept onderdeel van is.
        skos_top_concept_of (DeeltrajectConceptSKOSTopConceptOf | Unset): Verwijzing naar waar het meest abstracte
            concept van dit concept.
    """

    id: DeeltrajectConceptId
    type_: DeeltrajectConceptType
    skos_pref_label: DeeltrajectConceptSKOSPrefLabel
    skos_definition: DeeltrajectConceptSKOSDefinition
    skos_inscheme: DeeltrajectConceptSKOSInscheme | Unset = UNSET
    skos_top_concept_of: DeeltrajectConceptSKOSTopConceptOf | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        type_ = self.type_.value

        skos_pref_label = self.skos_pref_label.to_dict()

        skos_definition = self.skos_definition.to_dict()

        skos_inscheme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skos_inscheme, Unset):
            skos_inscheme = self.skos_inscheme.to_dict()

        skos_top_concept_of: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skos_top_concept_of, Unset):
            skos_top_concept_of = self.skos_top_concept_of.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
                "SKOS.prefLabel": skos_pref_label,
                "SKOS.definition": skos_definition,
            }
        )
        if skos_inscheme is not UNSET:
            field_dict["SKOS.inscheme"] = skos_inscheme
        if skos_top_concept_of is not UNSET:
            field_dict["SKOS.topConceptOf"] = skos_top_concept_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deeltraject_concept_skos_definition import DeeltrajectConceptSKOSDefinition
        from ..models.deeltraject_concept_skos_inscheme import DeeltrajectConceptSKOSInscheme
        from ..models.deeltraject_concept_skos_pref_label import DeeltrajectConceptSKOSPrefLabel
        from ..models.deeltraject_concept_skos_top_concept_of import DeeltrajectConceptSKOSTopConceptOf

        d = dict(src_dict)
        id = DeeltrajectConceptId(d.pop("@id"))

        type_ = DeeltrajectConceptType(d.pop("@type"))

        skos_pref_label = DeeltrajectConceptSKOSPrefLabel.from_dict(d.pop("SKOS.prefLabel"))

        skos_definition = DeeltrajectConceptSKOSDefinition.from_dict(d.pop("SKOS.definition"))

        _skos_inscheme = d.pop("SKOS.inscheme", UNSET)
        skos_inscheme: DeeltrajectConceptSKOSInscheme | Unset
        if isinstance(_skos_inscheme, Unset):
            skos_inscheme = UNSET
        else:
            skos_inscheme = DeeltrajectConceptSKOSInscheme.from_dict(_skos_inscheme)

        _skos_top_concept_of = d.pop("SKOS.topConceptOf", UNSET)
        skos_top_concept_of: DeeltrajectConceptSKOSTopConceptOf | Unset
        if isinstance(_skos_top_concept_of, Unset):
            skos_top_concept_of = UNSET
        else:
            skos_top_concept_of = DeeltrajectConceptSKOSTopConceptOf.from_dict(_skos_top_concept_of)

        deeltraject_concept = cls(
            id=id,
            type_=type_,
            skos_pref_label=skos_pref_label,
            skos_definition=skos_definition,
            skos_inscheme=skos_inscheme,
            skos_top_concept_of=skos_top_concept_of,
        )

        deeltraject_concept.additional_properties = d
        return deeltraject_concept

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
