from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.beroepstoestand_type import BeroepstoestandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.beroepstoestand_beroepstoestand_naam import BeroepstoestandBeroepstoestandNaam
    from ..models.beroepstoestand_beroepstoestand_voorkeur import BeroepstoestandBeroepstoestandVoorkeur


T = TypeVar("T", bound="Beroepstoestand")


@_attrs_define
class Beroepstoestand:
    """Voorkeur voor een bepaald beroep.

    Attributes:
        type_ (BeroepstoestandType): Object type.
        beroepstoestand_naam (BeroepstoestandBeroepstoestandNaam | Unset): Naam van het beroep.
        beroepstoestand_voorkeur (BeroepstoestandBeroepstoestandVoorkeur | Unset): De soort voorkeur voor een bepaald
            beroep.
    """

    type_: BeroepstoestandType
    beroepstoestand_naam: BeroepstoestandBeroepstoestandNaam | Unset = UNSET
    beroepstoestand_voorkeur: BeroepstoestandBeroepstoestandVoorkeur | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        beroepstoestand_naam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.beroepstoestand_naam, Unset):
            beroepstoestand_naam = self.beroepstoestand_naam.to_dict()

        beroepstoestand_voorkeur: dict[str, Any] | Unset = UNSET
        if not isinstance(self.beroepstoestand_voorkeur, Unset):
            beroepstoestand_voorkeur = self.beroepstoestand_voorkeur.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@type": type_,
            }
        )
        if beroepstoestand_naam is not UNSET:
            field_dict["Beroepstoestand.naam"] = beroepstoestand_naam
        if beroepstoestand_voorkeur is not UNSET:
            field_dict["Beroepstoestand.voorkeur"] = beroepstoestand_voorkeur

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.beroepstoestand_beroepstoestand_naam import BeroepstoestandBeroepstoestandNaam
        from ..models.beroepstoestand_beroepstoestand_voorkeur import BeroepstoestandBeroepstoestandVoorkeur

        d = dict(src_dict)
        type_ = BeroepstoestandType(d.pop("@type"))

        _beroepstoestand_naam = d.pop("Beroepstoestand.naam", UNSET)
        beroepstoestand_naam: BeroepstoestandBeroepstoestandNaam | Unset
        if isinstance(_beroepstoestand_naam, Unset):
            beroepstoestand_naam = UNSET
        else:
            beroepstoestand_naam = BeroepstoestandBeroepstoestandNaam.from_dict(_beroepstoestand_naam)

        _beroepstoestand_voorkeur = d.pop("Beroepstoestand.voorkeur", UNSET)
        beroepstoestand_voorkeur: BeroepstoestandBeroepstoestandVoorkeur | Unset
        if isinstance(_beroepstoestand_voorkeur, Unset):
            beroepstoestand_voorkeur = UNSET
        else:
            beroepstoestand_voorkeur = BeroepstoestandBeroepstoestandVoorkeur.from_dict(_beroepstoestand_voorkeur)

        beroepstoestand = cls(
            type_=type_,
            beroepstoestand_naam=beroepstoestand_naam,
            beroepstoestand_voorkeur=beroepstoestand_voorkeur,
        )

        beroepstoestand.additional_properties = d
        return beroepstoestand

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
