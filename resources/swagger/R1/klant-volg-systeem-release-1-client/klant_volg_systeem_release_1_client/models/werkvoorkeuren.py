from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.werkvoorkeuren_type import WerkvoorkeurenType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.beroepstoestand import Beroepstoestand


T = TypeVar("T", bound="Werkvoorkeuren")


@_attrs_define
class Werkvoorkeuren:
    """De voorkeuren van de Werkzoekende bij het zoeken naar werk.

    Attributes:
        id (str): Object ID. Can be an URI or internal reference such as _:MyID.
        type_ (WerkvoorkeurenType): Object type.
        werkvoorkeuren_beroep (list[Beroepstoestand] | Unset): Voorkeuren voor bepaalde beroepen.
    """

    id: str
    type_: WerkvoorkeurenType
    werkvoorkeuren_beroep: list[Beroepstoestand] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        werkvoorkeuren_beroep: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.werkvoorkeuren_beroep, Unset):
            werkvoorkeuren_beroep = []
            for werkvoorkeuren_beroep_item_data in self.werkvoorkeuren_beroep:
                werkvoorkeuren_beroep_item = werkvoorkeuren_beroep_item_data.to_dict()
                werkvoorkeuren_beroep.append(werkvoorkeuren_beroep_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
            }
        )
        if werkvoorkeuren_beroep is not UNSET:
            field_dict["Werkvoorkeuren.beroep"] = werkvoorkeuren_beroep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.beroepstoestand import Beroepstoestand

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = WerkvoorkeurenType(d.pop("@type"))

        _werkvoorkeuren_beroep = d.pop("Werkvoorkeuren.beroep", UNSET)
        werkvoorkeuren_beroep: list[Beroepstoestand] | Unset = UNSET
        if _werkvoorkeuren_beroep is not UNSET:
            werkvoorkeuren_beroep = []
            for werkvoorkeuren_beroep_item_data in _werkvoorkeuren_beroep:
                werkvoorkeuren_beroep_item = Beroepstoestand.from_dict(werkvoorkeuren_beroep_item_data)

                werkvoorkeuren_beroep.append(werkvoorkeuren_beroep_item)

        werkvoorkeuren = cls(
            id=id,
            type_=type_,
            werkvoorkeuren_beroep=werkvoorkeuren_beroep,
        )

        werkvoorkeuren.additional_properties = d
        return werkvoorkeuren

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
