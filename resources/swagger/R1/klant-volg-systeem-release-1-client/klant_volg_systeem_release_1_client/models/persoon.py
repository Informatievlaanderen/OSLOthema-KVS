from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.persoon_type import PersoonType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactpunt import Contactpunt
    from ..models.inwonerschap import Inwonerschap


T = TypeVar("T", bound="Persoon")


@_attrs_define
class Persoon:
    """Natuurlijk persoon.

    Attributes:
        id (str): Object ID. Can be an URI or internal reference such as _:MyID.
        type_ (PersoonType): Object type.
        persoon_voornaam (str | Unset): Naam die een Persoon bij geboorte wordt gegeven. Onderscheidt de Persoon van de
            andere personen in de familie.
        persoon_achternaam (str | Unset): Gedeelte van de volledige naam van de Persoon ontvangen van de vorige
            generatie.
        persoon_contactinfo (list[Contactpunt] | Unset): Informatie zoals email, telefoon... die toelaat de Persoon te
            contacteren.
        persoon_inwonerschap (list[Inwonerschap] | Unset): Jurisdictie waarbinnen het Inwonerschap van de Persoon is
            gedefinieerd.
    """

    id: str
    type_: PersoonType
    persoon_voornaam: str | Unset = UNSET
    persoon_achternaam: str | Unset = UNSET
    persoon_contactinfo: list[Contactpunt] | Unset = UNSET
    persoon_inwonerschap: list[Inwonerschap] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        persoon_voornaam = self.persoon_voornaam

        persoon_achternaam = self.persoon_achternaam

        persoon_contactinfo: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.persoon_contactinfo, Unset):
            persoon_contactinfo = []
            for persoon_contactinfo_item_data in self.persoon_contactinfo:
                persoon_contactinfo_item = persoon_contactinfo_item_data.to_dict()
                persoon_contactinfo.append(persoon_contactinfo_item)

        persoon_inwonerschap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.persoon_inwonerschap, Unset):
            persoon_inwonerschap = []
            for persoon_inwonerschap_item_data in self.persoon_inwonerschap:
                persoon_inwonerschap_item = persoon_inwonerschap_item_data.to_dict()
                persoon_inwonerschap.append(persoon_inwonerschap_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
            }
        )
        if persoon_voornaam is not UNSET:
            field_dict["Persoon.voornaam"] = persoon_voornaam
        if persoon_achternaam is not UNSET:
            field_dict["Persoon.achternaam"] = persoon_achternaam
        if persoon_contactinfo is not UNSET:
            field_dict["Persoon.contactinfo"] = persoon_contactinfo
        if persoon_inwonerschap is not UNSET:
            field_dict["Persoon.inwonerschap"] = persoon_inwonerschap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactpunt import Contactpunt
        from ..models.inwonerschap import Inwonerschap

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = PersoonType(d.pop("@type"))

        persoon_voornaam = d.pop("Persoon.voornaam", UNSET)

        persoon_achternaam = d.pop("Persoon.achternaam", UNSET)

        _persoon_contactinfo = d.pop("Persoon.contactinfo", UNSET)
        persoon_contactinfo: list[Contactpunt] | Unset = UNSET
        if _persoon_contactinfo is not UNSET:
            persoon_contactinfo = []
            for persoon_contactinfo_item_data in _persoon_contactinfo:
                persoon_contactinfo_item = Contactpunt.from_dict(persoon_contactinfo_item_data)

                persoon_contactinfo.append(persoon_contactinfo_item)

        _persoon_inwonerschap = d.pop("Persoon.inwonerschap", UNSET)
        persoon_inwonerschap: list[Inwonerschap] | Unset = UNSET
        if _persoon_inwonerschap is not UNSET:
            persoon_inwonerschap = []
            for persoon_inwonerschap_item_data in _persoon_inwonerschap:
                persoon_inwonerschap_item = Inwonerschap.from_dict(persoon_inwonerschap_item_data)

                persoon_inwonerschap.append(persoon_inwonerschap_item)

        persoon = cls(
            id=id,
            type_=type_,
            persoon_voornaam=persoon_voornaam,
            persoon_achternaam=persoon_achternaam,
            persoon_contactinfo=persoon_contactinfo,
            persoon_inwonerschap=persoon_inwonerschap,
        )

        persoon.additional_properties = d
        return persoon

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
