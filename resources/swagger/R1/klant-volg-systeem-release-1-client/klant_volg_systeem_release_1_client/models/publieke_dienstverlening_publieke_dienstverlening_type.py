from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publieke_dienstverlening_publieke_dienstverlening_type_id import (
    PubliekeDienstverleningPubliekeDienstverleningTypeId,
)

if TYPE_CHECKING:
    from ..models.publieke_dienstverlening_publieke_dienstverlening_type_skos_pref_label import (
        PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel,
    )


T = TypeVar("T", bound="PubliekeDienstverleningPubliekeDienstverleningType")


@_attrs_define
class PubliekeDienstverleningPubliekeDienstverleningType:
    """Het soort Publieke Dienstverlening.

    Attributes:
        id (PubliekeDienstverleningPubliekeDienstverleningTypeId): Object ID. Can be an URI or internal reference such
            as _:MyID. Must point to a PubliekeDienstverleningType enum value URI.
        skos_pref_label (PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel):
    """

    id: PubliekeDienstverleningPubliekeDienstverleningTypeId
    skos_pref_label: PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        skos_pref_label = self.skos_pref_label.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "SKOS.prefLabel": skos_pref_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publieke_dienstverlening_publieke_dienstverlening_type_skos_pref_label import (
            PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel,
        )

        d = dict(src_dict)
        id = PubliekeDienstverleningPubliekeDienstverleningTypeId(d.pop("@id"))

        skos_pref_label = PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel.from_dict(
            d.pop("SKOS.prefLabel")
        )

        publieke_dienstverlening_publieke_dienstverlening_type = cls(
            id=id,
            skos_pref_label=skos_pref_label,
        )

        publieke_dienstverlening_publieke_dienstverlening_type.additional_properties = d
        return publieke_dienstverlening_publieke_dienstverlening_type

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
