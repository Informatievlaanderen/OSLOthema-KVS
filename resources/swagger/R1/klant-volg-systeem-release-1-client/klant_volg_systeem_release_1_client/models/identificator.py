from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identificator_type import IdentificatorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Identificator")


@_attrs_define
class Identificator:
    """Informatie gebruikt om een object uniek te identificeren.

    Attributes:
        type_ (IdentificatorType): Object type.
        identificator_identificator (str | Unset): String gebruikt om het object uniek te identificeren.
        identificator_toegekend_door_string (str | Unset): Naam vd agent die de identificator heeft toegekend.
    """

    type_: IdentificatorType
    identificator_identificator: str | Unset = UNSET
    identificator_toegekend_door_string: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        identificator_identificator = self.identificator_identificator

        identificator_toegekend_door_string = self.identificator_toegekend_door_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@type": type_,
            }
        )
        if identificator_identificator is not UNSET:
            field_dict["Identificator.identificator"] = identificator_identificator
        if identificator_toegekend_door_string is not UNSET:
            field_dict["Identificator.toegekendDoor(String)"] = identificator_toegekend_door_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = IdentificatorType(d.pop("@type"))

        identificator_identificator = d.pop("Identificator.identificator", UNSET)

        identificator_toegekend_door_string = d.pop("Identificator.toegekendDoor(String)", UNSET)

        identificator = cls(
            type_=type_,
            identificator_identificator=identificator_identificator,
            identificator_toegekend_door_string=identificator_toegekend_door_string,
        )

        identificator.additional_properties = d
        return identificator

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
