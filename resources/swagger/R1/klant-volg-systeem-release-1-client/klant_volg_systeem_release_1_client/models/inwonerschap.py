from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inwonerschap_type import InwonerschapType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domicilie import Domicilie
    from ..models.verblijfplaats import Verblijfplaats


T = TypeVar("T", bound="Inwonerschap")


@_attrs_define
class Inwonerschap:
    """Het feit dat een persoon verblijf houdt in een plaats of land.

    Attributes:
        type_ (InwonerschapType | Unset): Object type.
        heeft_verblijfplaats (Domicilie | Unset | Verblijfplaats): Plaats waar een persoon verblijft.
    """

    type_: InwonerschapType | Unset = UNSET
    heeft_verblijfplaats: Domicilie | Unset | Verblijfplaats = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.verblijfplaats import Verblijfplaats

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        heeft_verblijfplaats: dict[str, Any] | Unset
        if isinstance(self.heeft_verblijfplaats, Unset):
            heeft_verblijfplaats = UNSET
        elif isinstance(self.heeft_verblijfplaats, Verblijfplaats):
            heeft_verblijfplaats = self.heeft_verblijfplaats.to_dict()
        else:
            heeft_verblijfplaats = self.heeft_verblijfplaats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["@type"] = type_
        if heeft_verblijfplaats is not UNSET:
            field_dict["heeftVerblijfplaats"] = heeft_verblijfplaats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domicilie import Domicilie
        from ..models.verblijfplaats import Verblijfplaats

        d = dict(src_dict)
        _type_ = d.pop("@type", UNSET)
        type_: InwonerschapType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InwonerschapType(_type_)

        def _parse_heeft_verblijfplaats(data: object) -> Domicilie | Unset | Verblijfplaats:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                heeft_verblijfplaats_type_0 = Verblijfplaats.from_dict(data)

                return heeft_verblijfplaats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            heeft_verblijfplaats_type_1 = Domicilie.from_dict(data)

            return heeft_verblijfplaats_type_1

        heeft_verblijfplaats = _parse_heeft_verblijfplaats(d.pop("heeftVerblijfplaats", UNSET))

        inwonerschap = cls(
            type_=type_,
            heeft_verblijfplaats=heeft_verblijfplaats,
        )

        inwonerschap.additional_properties = d
        return inwonerschap

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
