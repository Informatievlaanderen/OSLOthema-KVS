from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deeltraject_deeltraject_einddatum_type import DeeltrajectDeeltrajectEinddatumType

T = TypeVar("T", bound="DeeltrajectDeeltrajectEinddatum")


@_attrs_define
class DeeltrajectDeeltrajectEinddatum:
    """De datum waarop het Deeltraject eindigt.

    Attributes:
        value (datetime.datetime): JSON-LD's Literal ISO XSD.DateTime value.
        type_ (DeeltrajectDeeltrajectEinddatumType): Literal datatype fixed to XSD's DateTime.
    """

    value: datetime.datetime
    type_: DeeltrajectDeeltrajectEinddatumType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.isoformat()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@value": value,
                "@type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = isoparse(d.pop("@value"))

        type_ = DeeltrajectDeeltrajectEinddatumType(d.pop("@type"))

        deeltraject_deeltraject_einddatum = cls(
            value=value,
            type_=type_,
        )

        deeltraject_deeltraject_einddatum.additional_properties = d
        return deeltraject_deeltraject_einddatum

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
