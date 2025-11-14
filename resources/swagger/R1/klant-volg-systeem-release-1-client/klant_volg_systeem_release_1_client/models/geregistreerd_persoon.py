from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geregistreerd_persoon_type import GeregistreerdPersoonType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactpunt import Contactpunt
    from ..models.geregistreerd_persoon_geregistreerd_persoon_werkvoorkeuren_item import (
        GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenItem,
    )
    from ..models.identificator import Identificator
    from ..models.inwonerschap import Inwonerschap


T = TypeVar("T", bound="GeregistreerdPersoon")


@_attrs_define
class GeregistreerdPersoon:
    """Persoon waarvan de gegevens zijn ingeschreven in een register.

    Attributes:
        id (str): Object ID. Can be an URI or internal reference such as _:MyID.
        type_ (GeregistreerdPersoonType): Object type.
        geregistreerd_persoon_registratie (list[Identificator]): Identificatiecode van de persoon in het register.
        geregistreerd_persoon_voornaam (str | Unset): Naam die een Persoon bij geboorte wordt gegeven. Onderscheidt de
            Persoon van de andere personen in de familie.
        geregistreerd_persoon_achternaam (str | Unset): Gedeelte van de volledige naam van de Persoon ontvangen van de
            vorige generatie.
        geregistreerd_persoon_werkvoorkeuren (list[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenItem] | Unset):
            De voorkeuren voor werk van een Persoon.
        geregistreerd_persoon_contactinfo (list[Contactpunt] | Unset): Informatie zoals email, telefoon... die toelaat
            de Persoon te contacteren.
        geregistreerd_persoon_inwonerschap (list[Inwonerschap] | Unset): Jurisdictie waarbinnen het Inwonerschap van de
            Persoon is gedefinieerd.
    """

    id: str
    type_: GeregistreerdPersoonType
    geregistreerd_persoon_registratie: list[Identificator]
    geregistreerd_persoon_voornaam: str | Unset = UNSET
    geregistreerd_persoon_achternaam: str | Unset = UNSET
    geregistreerd_persoon_werkvoorkeuren: list[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenItem] | Unset = (
        UNSET
    )
    geregistreerd_persoon_contactinfo: list[Contactpunt] | Unset = UNSET
    geregistreerd_persoon_inwonerschap: list[Inwonerschap] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        geregistreerd_persoon_registratie = []
        for geregistreerd_persoon_registratie_item_data in self.geregistreerd_persoon_registratie:
            geregistreerd_persoon_registratie_item = geregistreerd_persoon_registratie_item_data.to_dict()
            geregistreerd_persoon_registratie.append(geregistreerd_persoon_registratie_item)

        geregistreerd_persoon_voornaam = self.geregistreerd_persoon_voornaam

        geregistreerd_persoon_achternaam = self.geregistreerd_persoon_achternaam

        geregistreerd_persoon_werkvoorkeuren: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geregistreerd_persoon_werkvoorkeuren, Unset):
            geregistreerd_persoon_werkvoorkeuren = []
            for geregistreerd_persoon_werkvoorkeuren_item_data in self.geregistreerd_persoon_werkvoorkeuren:
                geregistreerd_persoon_werkvoorkeuren_item = geregistreerd_persoon_werkvoorkeuren_item_data.to_dict()
                geregistreerd_persoon_werkvoorkeuren.append(geregistreerd_persoon_werkvoorkeuren_item)

        geregistreerd_persoon_contactinfo: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geregistreerd_persoon_contactinfo, Unset):
            geregistreerd_persoon_contactinfo = []
            for geregistreerd_persoon_contactinfo_item_data in self.geregistreerd_persoon_contactinfo:
                geregistreerd_persoon_contactinfo_item = geregistreerd_persoon_contactinfo_item_data.to_dict()
                geregistreerd_persoon_contactinfo.append(geregistreerd_persoon_contactinfo_item)

        geregistreerd_persoon_inwonerschap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geregistreerd_persoon_inwonerschap, Unset):
            geregistreerd_persoon_inwonerschap = []
            for geregistreerd_persoon_inwonerschap_item_data in self.geregistreerd_persoon_inwonerschap:
                geregistreerd_persoon_inwonerschap_item = geregistreerd_persoon_inwonerschap_item_data.to_dict()
                geregistreerd_persoon_inwonerschap.append(geregistreerd_persoon_inwonerschap_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
                "GeregistreerdPersoon.registratie": geregistreerd_persoon_registratie,
            }
        )
        if geregistreerd_persoon_voornaam is not UNSET:
            field_dict["GeregistreerdPersoon.voornaam"] = geregistreerd_persoon_voornaam
        if geregistreerd_persoon_achternaam is not UNSET:
            field_dict["GeregistreerdPersoon.achternaam"] = geregistreerd_persoon_achternaam
        if geregistreerd_persoon_werkvoorkeuren is not UNSET:
            field_dict["GeregistreerdPersoon.werkvoorkeuren"] = geregistreerd_persoon_werkvoorkeuren
        if geregistreerd_persoon_contactinfo is not UNSET:
            field_dict["GeregistreerdPersoon.contactinfo"] = geregistreerd_persoon_contactinfo
        if geregistreerd_persoon_inwonerschap is not UNSET:
            field_dict["GeregistreerdPersoon.inwonerschap"] = geregistreerd_persoon_inwonerschap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactpunt import Contactpunt
        from ..models.geregistreerd_persoon_geregistreerd_persoon_werkvoorkeuren_item import (
            GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenItem,
        )
        from ..models.identificator import Identificator
        from ..models.inwonerschap import Inwonerschap

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = GeregistreerdPersoonType(d.pop("@type"))

        geregistreerd_persoon_registratie = []
        _geregistreerd_persoon_registratie = d.pop("GeregistreerdPersoon.registratie")
        for geregistreerd_persoon_registratie_item_data in _geregistreerd_persoon_registratie:
            geregistreerd_persoon_registratie_item = Identificator.from_dict(
                geregistreerd_persoon_registratie_item_data
            )

            geregistreerd_persoon_registratie.append(geregistreerd_persoon_registratie_item)

        geregistreerd_persoon_voornaam = d.pop("GeregistreerdPersoon.voornaam", UNSET)

        geregistreerd_persoon_achternaam = d.pop("GeregistreerdPersoon.achternaam", UNSET)

        _geregistreerd_persoon_werkvoorkeuren = d.pop("GeregistreerdPersoon.werkvoorkeuren", UNSET)
        geregistreerd_persoon_werkvoorkeuren: (
            list[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenItem] | Unset
        ) = UNSET
        if _geregistreerd_persoon_werkvoorkeuren is not UNSET:
            geregistreerd_persoon_werkvoorkeuren = []
            for geregistreerd_persoon_werkvoorkeuren_item_data in _geregistreerd_persoon_werkvoorkeuren:
                geregistreerd_persoon_werkvoorkeuren_item = (
                    GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenItem.from_dict(
                        geregistreerd_persoon_werkvoorkeuren_item_data
                    )
                )

                geregistreerd_persoon_werkvoorkeuren.append(geregistreerd_persoon_werkvoorkeuren_item)

        _geregistreerd_persoon_contactinfo = d.pop("GeregistreerdPersoon.contactinfo", UNSET)
        geregistreerd_persoon_contactinfo: list[Contactpunt] | Unset = UNSET
        if _geregistreerd_persoon_contactinfo is not UNSET:
            geregistreerd_persoon_contactinfo = []
            for geregistreerd_persoon_contactinfo_item_data in _geregistreerd_persoon_contactinfo:
                geregistreerd_persoon_contactinfo_item = Contactpunt.from_dict(
                    geregistreerd_persoon_contactinfo_item_data
                )

                geregistreerd_persoon_contactinfo.append(geregistreerd_persoon_contactinfo_item)

        _geregistreerd_persoon_inwonerschap = d.pop("GeregistreerdPersoon.inwonerschap", UNSET)
        geregistreerd_persoon_inwonerschap: list[Inwonerschap] | Unset = UNSET
        if _geregistreerd_persoon_inwonerschap is not UNSET:
            geregistreerd_persoon_inwonerschap = []
            for geregistreerd_persoon_inwonerschap_item_data in _geregistreerd_persoon_inwonerschap:
                geregistreerd_persoon_inwonerschap_item = Inwonerschap.from_dict(
                    geregistreerd_persoon_inwonerschap_item_data
                )

                geregistreerd_persoon_inwonerschap.append(geregistreerd_persoon_inwonerschap_item)

        geregistreerd_persoon = cls(
            id=id,
            type_=type_,
            geregistreerd_persoon_registratie=geregistreerd_persoon_registratie,
            geregistreerd_persoon_voornaam=geregistreerd_persoon_voornaam,
            geregistreerd_persoon_achternaam=geregistreerd_persoon_achternaam,
            geregistreerd_persoon_werkvoorkeuren=geregistreerd_persoon_werkvoorkeuren,
            geregistreerd_persoon_contactinfo=geregistreerd_persoon_contactinfo,
            geregistreerd_persoon_inwonerschap=geregistreerd_persoon_inwonerschap,
        )

        geregistreerd_persoon.additional_properties = d
        return geregistreerd_persoon

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
