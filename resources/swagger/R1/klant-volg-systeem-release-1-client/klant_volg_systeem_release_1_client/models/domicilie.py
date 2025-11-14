from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domicilie_type import DomicilieType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domicilie_verblijfplaats_verblijfsadres import DomicilieVerblijfplaatsVerblijfsadres


T = TypeVar("T", bound="Domicilie")


@_attrs_define
class Domicilie:
    """Plaats waar een Persoon al dan niet tijdelijk woont of logeert. Specifieker type van Verblijfplaats, erft alle
    attributen over.

        Attributes:
            type_ (DomicilieType | Unset): Object type.
            verblijfplaats_verblijfsadres (DomicilieVerblijfplaatsVerblijfsadres | Unset): Adres dat men kan aanschrijven of
                bezoeken.
    """

    type_: DomicilieType | Unset = UNSET
    verblijfplaats_verblijfsadres: DomicilieVerblijfplaatsVerblijfsadres | Unset = UNSET
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
        from ..models.domicilie_verblijfplaats_verblijfsadres import DomicilieVerblijfplaatsVerblijfsadres

        d = dict(src_dict)
        _type_ = d.pop("@type", UNSET)
        type_: DomicilieType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DomicilieType(_type_)

        _verblijfplaats_verblijfsadres = d.pop("Verblijfplaats.verblijfsadres", UNSET)
        verblijfplaats_verblijfsadres: DomicilieVerblijfplaatsVerblijfsadres | Unset
        if isinstance(_verblijfplaats_verblijfsadres, Unset):
            verblijfplaats_verblijfsadres = UNSET
        else:
            verblijfplaats_verblijfsadres = DomicilieVerblijfplaatsVerblijfsadres.from_dict(
                _verblijfplaats_verblijfsadres
            )

        domicilie = cls(
            type_=type_,
            verblijfplaats_verblijfsadres=verblijfplaats_verblijfsadres,
        )

        domicilie.additional_properties = d
        return domicilie

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
