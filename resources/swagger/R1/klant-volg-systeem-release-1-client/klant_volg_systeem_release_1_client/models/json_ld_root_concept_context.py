from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_ld_root_concept_context_skos import JsonLdRootConceptContextSKOS
from ..types import UNSET, Unset

T = TypeVar("T", bound="JsonLdRootConceptContext")


@_attrs_define
class JsonLdRootConceptContext:
    """JSON-LD's context which defines how the JSON-LD keys are mapped to URIs.

    Attributes:
        skos (JsonLdRootConceptContextSKOS | Unset): W3C SKOS vocabulary URI.
    """

    skos: JsonLdRootConceptContextSKOS | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skos: str | Unset = UNSET
        if not isinstance(self.skos, Unset):
            skos = self.skos.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skos is not UNSET:
            field_dict["SKOS"] = skos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _skos = d.pop("SKOS", UNSET)
        skos: JsonLdRootConceptContextSKOS | Unset
        if isinstance(_skos, Unset):
            skos = UNSET
        else:
            skos = JsonLdRootConceptContextSKOS(_skos)

        json_ld_root_concept_context = cls(
            skos=skos,
        )

        json_ld_root_concept_context.additional_properties = d
        return json_ld_root_concept_context

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
