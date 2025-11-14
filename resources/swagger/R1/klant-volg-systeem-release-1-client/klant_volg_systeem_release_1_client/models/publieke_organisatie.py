from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publieke_organisatie_type import PubliekeOrganisatieType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactpunt import Contactpunt
    from ..models.identificator import Identificator
    from ..models.publieke_organisatie_publieke_organisatie_type import PubliekeOrganisatiePubliekeOrganisatieType
    from ..models.publieke_organisatie_publieke_organisatie_voorkeursnaam import (
        PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam,
    )


T = TypeVar("T", bound="PubliekeOrganisatie")


@_attrs_define
class PubliekeOrganisatie:
    """Een Organisatie die volgens een wettelijk kader behoort tot de publieke sector, ongeacht het bestuursniveau waarop
    dat kader van kracht is.

        Attributes:
            id (str): Object ID. Can be an URI or internal reference such as _:MyID.
            type_ (PubliekeOrganisatieType): Object type.
            publieke_organisatie_voorkeursnaam (PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam | Unset): Naam waarmee
                de Organisatie bij voorkeur wordt aangeduid.
            publieke_organisatie_contactinfo (list[Contactpunt] | Unset): Informatie zoals email, telefoon... die toelaat de
                Organisatie te contacteren.
            publieke_organisatie_identificator (list[Identificator] | Unset): Identificator die de organisatie uniek
                identificeert.
            publieke_organisatie_type (PubliekeOrganisatiePubliekeOrganisatieType | Unset): Het soort Organisatie.
    """

    id: str
    type_: PubliekeOrganisatieType
    publieke_organisatie_voorkeursnaam: PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam | Unset = UNSET
    publieke_organisatie_contactinfo: list[Contactpunt] | Unset = UNSET
    publieke_organisatie_identificator: list[Identificator] | Unset = UNSET
    publieke_organisatie_type: PubliekeOrganisatiePubliekeOrganisatieType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        publieke_organisatie_voorkeursnaam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publieke_organisatie_voorkeursnaam, Unset):
            publieke_organisatie_voorkeursnaam = self.publieke_organisatie_voorkeursnaam.to_dict()

        publieke_organisatie_contactinfo: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publieke_organisatie_contactinfo, Unset):
            publieke_organisatie_contactinfo = []
            for publieke_organisatie_contactinfo_item_data in self.publieke_organisatie_contactinfo:
                publieke_organisatie_contactinfo_item = publieke_organisatie_contactinfo_item_data.to_dict()
                publieke_organisatie_contactinfo.append(publieke_organisatie_contactinfo_item)

        publieke_organisatie_identificator: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publieke_organisatie_identificator, Unset):
            publieke_organisatie_identificator = []
            for publieke_organisatie_identificator_item_data in self.publieke_organisatie_identificator:
                publieke_organisatie_identificator_item = publieke_organisatie_identificator_item_data.to_dict()
                publieke_organisatie_identificator.append(publieke_organisatie_identificator_item)

        publieke_organisatie_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publieke_organisatie_type, Unset):
            publieke_organisatie_type = self.publieke_organisatie_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
            }
        )
        if publieke_organisatie_voorkeursnaam is not UNSET:
            field_dict["PubliekeOrganisatie.voorkeursnaam"] = publieke_organisatie_voorkeursnaam
        if publieke_organisatie_contactinfo is not UNSET:
            field_dict["PubliekeOrganisatie.contactinfo"] = publieke_organisatie_contactinfo
        if publieke_organisatie_identificator is not UNSET:
            field_dict["PubliekeOrganisatie.identificator"] = publieke_organisatie_identificator
        if publieke_organisatie_type is not UNSET:
            field_dict["PubliekeOrganisatie.type"] = publieke_organisatie_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactpunt import Contactpunt
        from ..models.identificator import Identificator
        from ..models.publieke_organisatie_publieke_organisatie_type import PubliekeOrganisatiePubliekeOrganisatieType
        from ..models.publieke_organisatie_publieke_organisatie_voorkeursnaam import (
            PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam,
        )

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = PubliekeOrganisatieType(d.pop("@type"))

        _publieke_organisatie_voorkeursnaam = d.pop("PubliekeOrganisatie.voorkeursnaam", UNSET)
        publieke_organisatie_voorkeursnaam: PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam | Unset
        if isinstance(_publieke_organisatie_voorkeursnaam, Unset):
            publieke_organisatie_voorkeursnaam = UNSET
        else:
            publieke_organisatie_voorkeursnaam = PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam.from_dict(
                _publieke_organisatie_voorkeursnaam
            )

        _publieke_organisatie_contactinfo = d.pop("PubliekeOrganisatie.contactinfo", UNSET)
        publieke_organisatie_contactinfo: list[Contactpunt] | Unset = UNSET
        if _publieke_organisatie_contactinfo is not UNSET:
            publieke_organisatie_contactinfo = []
            for publieke_organisatie_contactinfo_item_data in _publieke_organisatie_contactinfo:
                publieke_organisatie_contactinfo_item = Contactpunt.from_dict(
                    publieke_organisatie_contactinfo_item_data
                )

                publieke_organisatie_contactinfo.append(publieke_organisatie_contactinfo_item)

        _publieke_organisatie_identificator = d.pop("PubliekeOrganisatie.identificator", UNSET)
        publieke_organisatie_identificator: list[Identificator] | Unset = UNSET
        if _publieke_organisatie_identificator is not UNSET:
            publieke_organisatie_identificator = []
            for publieke_organisatie_identificator_item_data in _publieke_organisatie_identificator:
                publieke_organisatie_identificator_item = Identificator.from_dict(
                    publieke_organisatie_identificator_item_data
                )

                publieke_organisatie_identificator.append(publieke_organisatie_identificator_item)

        _publieke_organisatie_type = d.pop("PubliekeOrganisatie.type", UNSET)
        publieke_organisatie_type: PubliekeOrganisatiePubliekeOrganisatieType | Unset
        if isinstance(_publieke_organisatie_type, Unset):
            publieke_organisatie_type = UNSET
        else:
            publieke_organisatie_type = PubliekeOrganisatiePubliekeOrganisatieType.from_dict(_publieke_organisatie_type)

        publieke_organisatie = cls(
            id=id,
            type_=type_,
            publieke_organisatie_voorkeursnaam=publieke_organisatie_voorkeursnaam,
            publieke_organisatie_contactinfo=publieke_organisatie_contactinfo,
            publieke_organisatie_identificator=publieke_organisatie_identificator,
            publieke_organisatie_type=publieke_organisatie_type,
        )

        publieke_organisatie.additional_properties = d
        return publieke_organisatie

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
