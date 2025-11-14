from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deeltraject_concept_skos_pref_label_language import DeeltrajectConceptSKOSPrefLabelLanguage

T = TypeVar("T", bound="DeeltrajectConceptSKOSPrefLabel")


@_attrs_define
class DeeltrajectConceptSKOSPrefLabel:
    """Label van het concept.

    Attributes:
        value (str): JSON-LD's Literal string value.
        language (DeeltrajectConceptSKOSPrefLabelLanguage): The language in which the Literal string is written.
    """

    value: str
    language: DeeltrajectConceptSKOSPrefLabelLanguage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        language = self.language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@value": value,
                "@language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("@value")

        language = DeeltrajectConceptSKOSPrefLabelLanguage(d.pop("@language"))

        deeltraject_concept_skos_pref_label = cls(
            value=value,
            language=language,
        )

        deeltraject_concept_skos_pref_label.additional_properties = d
        return deeltraject_concept_skos_pref_label

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
