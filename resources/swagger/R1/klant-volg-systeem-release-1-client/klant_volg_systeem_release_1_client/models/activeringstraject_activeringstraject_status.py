from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activeringstraject_activeringstraject_status_id import ActiveringstrajectActiveringstrajectStatusId

if TYPE_CHECKING:
    from ..models.activeringstraject_activeringstraject_status_skos_pref_label import (
        ActiveringstrajectActiveringstrajectStatusSKOSPrefLabel,
    )


T = TypeVar("T", bound="ActiveringstrajectActiveringstrajectStatus")


@_attrs_define
class ActiveringstrajectActiveringstrajectStatus:
    """
    Attributes:
        id (ActiveringstrajectActiveringstrajectStatusId): Object ID. Can be an URI or internal reference such as
            _:MyID. Must point to a TrajectStatus enum value URI.
        skos_pref_label (ActiveringstrajectActiveringstrajectStatusSKOSPrefLabel):
    """

    id: ActiveringstrajectActiveringstrajectStatusId
    skos_pref_label: ActiveringstrajectActiveringstrajectStatusSKOSPrefLabel
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
        from ..models.activeringstraject_activeringstraject_status_skos_pref_label import (
            ActiveringstrajectActiveringstrajectStatusSKOSPrefLabel,
        )

        d = dict(src_dict)
        id = ActiveringstrajectActiveringstrajectStatusId(d.pop("@id"))

        skos_pref_label = ActiveringstrajectActiveringstrajectStatusSKOSPrefLabel.from_dict(d.pop("SKOS.prefLabel"))

        activeringstraject_activeringstraject_status = cls(
            id=id,
            skos_pref_label=skos_pref_label,
        )

        activeringstraject_activeringstraject_status.additional_properties = d
        return activeringstraject_activeringstraject_status

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
