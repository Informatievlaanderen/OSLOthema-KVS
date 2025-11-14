from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geregistreerde_organisatie_type import GeregistreerdeOrganisatieType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactpunt import Contactpunt
    from ..models.geregistreerde_organisatie_geregistreerde_organisatie_type import (
        GeregistreerdeOrganisatieGeregistreerdeOrganisatieType,
    )
    from ..models.geregistreerde_organisatie_geregistreerde_organisatie_voorkeursnaam import (
        GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam,
    )
    from ..models.identificator import Identificator


T = TypeVar("T", bound="GeregistreerdeOrganisatie")


@_attrs_define
class GeregistreerdeOrganisatie:
    """Organisatie met een juridisch statuut vastgelegd door registratie. Vergelijk met een FormeleOrganisatie waarbij dit
    statuut ook op een andere manier verkregen kan zijn.

        Attributes:
            id (str): Object ID. Can be an URI or internal reference such as _:MyID.
            type_ (GeregistreerdeOrganisatieType): Object type.
            geregistreerde_organisatie_registratie (list[Identificator]):
            geregistreerde_organisatie_voorkeursnaam (GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam |
                Unset): Naam waarmee de Organisatie bij voorkeur wordt aangeduid
            geregistreerde_organisatie_contactinfo (list[Contactpunt] | Unset): Informatie zoals email, telefoon... die
                toelaat de Organisatie te contacteren.
            geregistreerde_organisatie_type (GeregistreerdeOrganisatieGeregistreerdeOrganisatieType | Unset): Het soort
                Organisatie.
    """

    id: str
    type_: GeregistreerdeOrganisatieType
    geregistreerde_organisatie_registratie: list[Identificator]
    geregistreerde_organisatie_voorkeursnaam: (
        GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam | Unset
    ) = UNSET
    geregistreerde_organisatie_contactinfo: list[Contactpunt] | Unset = UNSET
    geregistreerde_organisatie_type: GeregistreerdeOrganisatieGeregistreerdeOrganisatieType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        geregistreerde_organisatie_registratie = []
        for geregistreerde_organisatie_registratie_item_data in self.geregistreerde_organisatie_registratie:
            geregistreerde_organisatie_registratie_item = geregistreerde_organisatie_registratie_item_data.to_dict()
            geregistreerde_organisatie_registratie.append(geregistreerde_organisatie_registratie_item)

        geregistreerde_organisatie_voorkeursnaam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geregistreerde_organisatie_voorkeursnaam, Unset):
            geregistreerde_organisatie_voorkeursnaam = self.geregistreerde_organisatie_voorkeursnaam.to_dict()

        geregistreerde_organisatie_contactinfo: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geregistreerde_organisatie_contactinfo, Unset):
            geregistreerde_organisatie_contactinfo = []
            for geregistreerde_organisatie_contactinfo_item_data in self.geregistreerde_organisatie_contactinfo:
                geregistreerde_organisatie_contactinfo_item = geregistreerde_organisatie_contactinfo_item_data.to_dict()
                geregistreerde_organisatie_contactinfo.append(geregistreerde_organisatie_contactinfo_item)

        geregistreerde_organisatie_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geregistreerde_organisatie_type, Unset):
            geregistreerde_organisatie_type = self.geregistreerde_organisatie_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
                "GeregistreerdeOrganisatie.registratie": geregistreerde_organisatie_registratie,
            }
        )
        if geregistreerde_organisatie_voorkeursnaam is not UNSET:
            field_dict["GeregistreerdeOrganisatie.voorkeursnaam"] = geregistreerde_organisatie_voorkeursnaam
        if geregistreerde_organisatie_contactinfo is not UNSET:
            field_dict["GeregistreerdeOrganisatie.contactinfo"] = geregistreerde_organisatie_contactinfo
        if geregistreerde_organisatie_type is not UNSET:
            field_dict["GeregistreerdeOrganisatie.type"] = geregistreerde_organisatie_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactpunt import Contactpunt
        from ..models.geregistreerde_organisatie_geregistreerde_organisatie_type import (
            GeregistreerdeOrganisatieGeregistreerdeOrganisatieType,
        )
        from ..models.geregistreerde_organisatie_geregistreerde_organisatie_voorkeursnaam import (
            GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam,
        )
        from ..models.identificator import Identificator

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = GeregistreerdeOrganisatieType(d.pop("@type"))

        geregistreerde_organisatie_registratie = []
        _geregistreerde_organisatie_registratie = d.pop("GeregistreerdeOrganisatie.registratie")
        for geregistreerde_organisatie_registratie_item_data in _geregistreerde_organisatie_registratie:
            geregistreerde_organisatie_registratie_item = Identificator.from_dict(
                geregistreerde_organisatie_registratie_item_data
            )

            geregistreerde_organisatie_registratie.append(geregistreerde_organisatie_registratie_item)

        _geregistreerde_organisatie_voorkeursnaam = d.pop("GeregistreerdeOrganisatie.voorkeursnaam", UNSET)
        geregistreerde_organisatie_voorkeursnaam: (
            GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam | Unset
        )
        if isinstance(_geregistreerde_organisatie_voorkeursnaam, Unset):
            geregistreerde_organisatie_voorkeursnaam = UNSET
        else:
            geregistreerde_organisatie_voorkeursnaam = (
                GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam.from_dict(
                    _geregistreerde_organisatie_voorkeursnaam
                )
            )

        _geregistreerde_organisatie_contactinfo = d.pop("GeregistreerdeOrganisatie.contactinfo", UNSET)
        geregistreerde_organisatie_contactinfo: list[Contactpunt] | Unset = UNSET
        if _geregistreerde_organisatie_contactinfo is not UNSET:
            geregistreerde_organisatie_contactinfo = []
            for geregistreerde_organisatie_contactinfo_item_data in _geregistreerde_organisatie_contactinfo:
                geregistreerde_organisatie_contactinfo_item = Contactpunt.from_dict(
                    geregistreerde_organisatie_contactinfo_item_data
                )

                geregistreerde_organisatie_contactinfo.append(geregistreerde_organisatie_contactinfo_item)

        _geregistreerde_organisatie_type = d.pop("GeregistreerdeOrganisatie.type", UNSET)
        geregistreerde_organisatie_type: GeregistreerdeOrganisatieGeregistreerdeOrganisatieType | Unset
        if isinstance(_geregistreerde_organisatie_type, Unset):
            geregistreerde_organisatie_type = UNSET
        else:
            geregistreerde_organisatie_type = GeregistreerdeOrganisatieGeregistreerdeOrganisatieType.from_dict(
                _geregistreerde_organisatie_type
            )

        geregistreerde_organisatie = cls(
            id=id,
            type_=type_,
            geregistreerde_organisatie_registratie=geregistreerde_organisatie_registratie,
            geregistreerde_organisatie_voorkeursnaam=geregistreerde_organisatie_voorkeursnaam,
            geregistreerde_organisatie_contactinfo=geregistreerde_organisatie_contactinfo,
            geregistreerde_organisatie_type=geregistreerde_organisatie_type,
        )

        geregistreerde_organisatie.additional_properties = d
        return geregistreerde_organisatie

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
