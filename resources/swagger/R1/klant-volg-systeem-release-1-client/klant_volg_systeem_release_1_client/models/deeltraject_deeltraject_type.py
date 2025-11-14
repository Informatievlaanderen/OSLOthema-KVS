from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deeltraject_deeltraject_type_id import DeeltrajectDeeltrajectTypeId

T = TypeVar("T", bound="DeeltrajectDeeltrajectType")


@_attrs_define
class DeeltrajectDeeltrajectType:
    """
    Attributes:
        id (DeeltrajectDeeltrajectTypeId): Object ID. Can be an URI or internal reference such as _:MyID. Must point to
            a Deeltrajecttype enum value URI.
    """

    id: DeeltrajectDeeltrajectTypeId
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = DeeltrajectDeeltrajectTypeId(d.pop("@id"))

        deeltraject_deeltraject_type = cls(
            id=id,
        )

        deeltraject_deeltraject_type.additional_properties = d
        return deeltraject_deeltraject_type

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
