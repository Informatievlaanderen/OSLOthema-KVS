from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verblijfplaats_type import VerblijfplaatsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verblijfplaats_verblijfplaats_verblijfsadres import VerblijfplaatsVerblijfplaatsVerblijfsadres


T = TypeVar("T", bound="Verblijfplaats")


@_attrs_define
class Verblijfplaats:
    """Plaats waar een Persoon al dan niet tijdelijk woont of logeert.

    Attributes:
        type_ (VerblijfplaatsType | Unset): Object type.
        verblijfplaats_verblijfsadres (VerblijfplaatsVerblijfplaatsVerblijfsadres | Unset): Adres dat men kan
            aanschrijven of bezoeken.
    """

    type_: VerblijfplaatsType | Unset = UNSET
    verblijfplaats_verblijfsadres: VerblijfplaatsVerblijfplaatsVerblijfsadres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        verblijfplaats_verblijfsadres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verblijfplaats_verblijfsadres, Unset):
            verblijfplaats_verblijfsadres = self.verblijfplaats_verblijfsadres.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["@type"] = type_
        if verblijfplaats_verblijfsadres is not UNSET:
            field_dict["Verblijfplaats.verblijfsadres"] = verblijfplaats_verblijfsadres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verblijfplaats_verblijfplaats_verblijfsadres import VerblijfplaatsVerblijfplaatsVerblijfsadres

        d = dict(src_dict)
        _type_ = d.pop("@type", UNSET)
        type_: VerblijfplaatsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VerblijfplaatsType(_type_)

        _verblijfplaats_verblijfsadres = d.pop("Verblijfplaats.verblijfsadres", UNSET)
        verblijfplaats_verblijfsadres: VerblijfplaatsVerblijfplaatsVerblijfsadres | Unset
        if isinstance(_verblijfplaats_verblijfsadres, Unset):
            verblijfplaats_verblijfsadres = UNSET
        else:
            verblijfplaats_verblijfsadres = VerblijfplaatsVerblijfplaatsVerblijfsadres.from_dict(
                _verblijfplaats_verblijfsadres
            )

        verblijfplaats = cls(
            type_=type_,
            verblijfplaats_verblijfsadres=verblijfplaats_verblijfsadres,
        )

        verblijfplaats.additional_properties = d
        return verblijfplaats

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
