from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deeltraject_deeltraject_status_id import DeeltrajectDeeltrajectStatusId

if TYPE_CHECKING:
    from ..models.deeltraject_deeltraject_status_skos_pref_label import DeeltrajectDeeltrajectStatusSKOSPrefLabel


T = TypeVar("T", bound="DeeltrajectDeeltrajectStatus")


@_attrs_define
class DeeltrajectDeeltrajectStatus:
    """
    Attributes:
        id (DeeltrajectDeeltrajectStatusId): Object ID. Can be an URI or internal reference such as _:MyID. Must point
            to a TrajectStatus enum value URI.
        skos_pref_label (DeeltrajectDeeltrajectStatusSKOSPrefLabel):
    """

    id: DeeltrajectDeeltrajectStatusId
    skos_pref_label: DeeltrajectDeeltrajectStatusSKOSPrefLabel
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
        from ..models.deeltraject_deeltraject_status_skos_pref_label import DeeltrajectDeeltrajectStatusSKOSPrefLabel

        d = dict(src_dict)
        id = DeeltrajectDeeltrajectStatusId(d.pop("@id"))

        skos_pref_label = DeeltrajectDeeltrajectStatusSKOSPrefLabel.from_dict(d.pop("SKOS.prefLabel"))

        deeltraject_deeltraject_status = cls(
            id=id,
            skos_pref_label=skos_pref_label,
        )

        deeltraject_deeltraject_status.additional_properties = d
        return deeltraject_deeltraject_status

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
