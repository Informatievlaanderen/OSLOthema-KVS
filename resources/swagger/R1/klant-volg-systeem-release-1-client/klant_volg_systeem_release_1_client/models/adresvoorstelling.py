from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.adresvoorstelling_type import AdresvoorstellingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adresvoorstelling_adresvoorstelling_busnummer import AdresvoorstellingAdresvoorstellingBusnummer
    from ..models.adresvoorstelling_adresvoorstelling_gemeentecode import AdresvoorstellingAdresvoorstellingGemeentecode
    from ..models.adresvoorstelling_adresvoorstelling_gemeentenaam import AdresvoorstellingAdresvoorstellingGemeentenaam
    from ..models.adresvoorstelling_adresvoorstelling_huisnummer import AdresvoorstellingAdresvoorstellingHuisnummer
    from ..models.adresvoorstelling_adresvoorstelling_land import AdresvoorstellingAdresvoorstellingLand
    from ..models.adresvoorstelling_adresvoorstelling_postcode import AdresvoorstellingAdresvoorstellingPostcode
    from ..models.adresvoorstelling_adresvoorstelling_straatcode import AdresvoorstellingAdresvoorstellingStraatcode
    from ..models.adresvoorstelling_adresvoorstelling_straatnaam import AdresvoorstellingAdresvoorstellingStraatnaam


T = TypeVar("T", bound="Adresvoorstelling")


@_attrs_define
class Adresvoorstelling:
    """Meer leesbare voorstelling met enkel de basisgegevens van het adres, bedoeld voor het gebruik van een adres als
    attribuut van een ander object.

        Attributes:
            type_ (AdresvoorstellingType): Object type.
            id (str | Unset): Object ID. Can be an URI or internal reference such as _:MyID.
            adresvoorstelling_straatnaam (AdresvoorstellingAdresvoorstellingStraatnaam | Unset): Straatnaam van het adres.
            adresvoorstelling_straatcode (AdresvoorstellingAdresvoorstellingStraatcode | Unset): De NIS code van de straat.
            adresvoorstelling_busnummer (AdresvoorstellingAdresvoorstellingBusnummer | Unset): Officieel toegekende
                alfanumerieke code die wordt toegevoegd aan het huisnummer om meerdere gebouweenheden, standplaatsen,
                ligplaatsen of percelen te onderscheiden die eenzelfde huisnummer hebben.
            adresvoorstelling_huisnummer (AdresvoorstellingAdresvoorstellingHuisnummer | Unset): Alfanumerieke code
                officieel toegekend aan gebouweenheden, ligplaatsen, standplaatsen of percelen.
            adresvoorstelling_postcode (AdresvoorstellingAdresvoorstellingPostcode | Unset): Code waarmee het geografisch
                gebied dat adressen voor postale doeleinden groepeert wordt aangeduid.
            adresvoorstelling_gemeentenaam (AdresvoorstellingAdresvoorstellingGemeentenaam | Unset): Gemeentenaam van het
                adres.
            adresvoorstelling_gemeentecode (AdresvoorstellingAdresvoorstellingGemeentecode | Unset): De NIS code van de
                gemeente.
            adresvoorstelling_land (AdresvoorstellingAdresvoorstellingLand | Unset): Land waarin het adres gelegen is.
    """

    type_: AdresvoorstellingType
    id: str | Unset = UNSET
    adresvoorstelling_straatnaam: AdresvoorstellingAdresvoorstellingStraatnaam | Unset = UNSET
    adresvoorstelling_straatcode: AdresvoorstellingAdresvoorstellingStraatcode | Unset = UNSET
    adresvoorstelling_busnummer: AdresvoorstellingAdresvoorstellingBusnummer | Unset = UNSET
    adresvoorstelling_huisnummer: AdresvoorstellingAdresvoorstellingHuisnummer | Unset = UNSET
    adresvoorstelling_postcode: AdresvoorstellingAdresvoorstellingPostcode | Unset = UNSET
    adresvoorstelling_gemeentenaam: AdresvoorstellingAdresvoorstellingGemeentenaam | Unset = UNSET
    adresvoorstelling_gemeentecode: AdresvoorstellingAdresvoorstellingGemeentecode | Unset = UNSET
    adresvoorstelling_land: AdresvoorstellingAdresvoorstellingLand | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        adresvoorstelling_straatnaam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_straatnaam, Unset):
            adresvoorstelling_straatnaam = self.adresvoorstelling_straatnaam.to_dict()

        adresvoorstelling_straatcode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_straatcode, Unset):
            adresvoorstelling_straatcode = self.adresvoorstelling_straatcode.to_dict()

        adresvoorstelling_busnummer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_busnummer, Unset):
            adresvoorstelling_busnummer = self.adresvoorstelling_busnummer.to_dict()

        adresvoorstelling_huisnummer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_huisnummer, Unset):
            adresvoorstelling_huisnummer = self.adresvoorstelling_huisnummer.to_dict()

        adresvoorstelling_postcode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_postcode, Unset):
            adresvoorstelling_postcode = self.adresvoorstelling_postcode.to_dict()

        adresvoorstelling_gemeentenaam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_gemeentenaam, Unset):
            adresvoorstelling_gemeentenaam = self.adresvoorstelling_gemeentenaam.to_dict()

        adresvoorstelling_gemeentecode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_gemeentecode, Unset):
            adresvoorstelling_gemeentecode = self.adresvoorstelling_gemeentecode.to_dict()

        adresvoorstelling_land: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adresvoorstelling_land, Unset):
            adresvoorstelling_land = self.adresvoorstelling_land.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@type": type_,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if adresvoorstelling_straatnaam is not UNSET:
            field_dict["Adresvoorstelling.straatnaam"] = adresvoorstelling_straatnaam
        if adresvoorstelling_straatcode is not UNSET:
            field_dict["Adresvoorstelling.straatcode"] = adresvoorstelling_straatcode
        if adresvoorstelling_busnummer is not UNSET:
            field_dict["Adresvoorstelling.busnummer"] = adresvoorstelling_busnummer
        if adresvoorstelling_huisnummer is not UNSET:
            field_dict["Adresvoorstelling.huisnummer"] = adresvoorstelling_huisnummer
        if adresvoorstelling_postcode is not UNSET:
            field_dict["Adresvoorstelling.postcode"] = adresvoorstelling_postcode
        if adresvoorstelling_gemeentenaam is not UNSET:
            field_dict["Adresvoorstelling.gemeentenaam"] = adresvoorstelling_gemeentenaam
        if adresvoorstelling_gemeentecode is not UNSET:
            field_dict["Adresvoorstelling.gemeentecode"] = adresvoorstelling_gemeentecode
        if adresvoorstelling_land is not UNSET:
            field_dict["Adresvoorstelling.land"] = adresvoorstelling_land

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adresvoorstelling_adresvoorstelling_busnummer import AdresvoorstellingAdresvoorstellingBusnummer
        from ..models.adresvoorstelling_adresvoorstelling_gemeentecode import (
            AdresvoorstellingAdresvoorstellingGemeentecode,
        )
        from ..models.adresvoorstelling_adresvoorstelling_gemeentenaam import (
            AdresvoorstellingAdresvoorstellingGemeentenaam,
        )
        from ..models.adresvoorstelling_adresvoorstelling_huisnummer import AdresvoorstellingAdresvoorstellingHuisnummer
        from ..models.adresvoorstelling_adresvoorstelling_land import AdresvoorstellingAdresvoorstellingLand
        from ..models.adresvoorstelling_adresvoorstelling_postcode import AdresvoorstellingAdresvoorstellingPostcode
        from ..models.adresvoorstelling_adresvoorstelling_straatcode import AdresvoorstellingAdresvoorstellingStraatcode
        from ..models.adresvoorstelling_adresvoorstelling_straatnaam import AdresvoorstellingAdresvoorstellingStraatnaam

        d = dict(src_dict)
        type_ = AdresvoorstellingType(d.pop("@type"))

        id = d.pop("@id", UNSET)

        _adresvoorstelling_straatnaam = d.pop("Adresvoorstelling.straatnaam", UNSET)
        adresvoorstelling_straatnaam: AdresvoorstellingAdresvoorstellingStraatnaam | Unset
        if isinstance(_adresvoorstelling_straatnaam, Unset):
            adresvoorstelling_straatnaam = UNSET
        else:
            adresvoorstelling_straatnaam = AdresvoorstellingAdresvoorstellingStraatnaam.from_dict(
                _adresvoorstelling_straatnaam
            )

        _adresvoorstelling_straatcode = d.pop("Adresvoorstelling.straatcode", UNSET)
        adresvoorstelling_straatcode: AdresvoorstellingAdresvoorstellingStraatcode | Unset
        if isinstance(_adresvoorstelling_straatcode, Unset):
            adresvoorstelling_straatcode = UNSET
        else:
            adresvoorstelling_straatcode = AdresvoorstellingAdresvoorstellingStraatcode.from_dict(
                _adresvoorstelling_straatcode
            )

        _adresvoorstelling_busnummer = d.pop("Adresvoorstelling.busnummer", UNSET)
        adresvoorstelling_busnummer: AdresvoorstellingAdresvoorstellingBusnummer | Unset
        if isinstance(_adresvoorstelling_busnummer, Unset):
            adresvoorstelling_busnummer = UNSET
        else:
            adresvoorstelling_busnummer = AdresvoorstellingAdresvoorstellingBusnummer.from_dict(
                _adresvoorstelling_busnummer
            )

        _adresvoorstelling_huisnummer = d.pop("Adresvoorstelling.huisnummer", UNSET)
        adresvoorstelling_huisnummer: AdresvoorstellingAdresvoorstellingHuisnummer | Unset
        if isinstance(_adresvoorstelling_huisnummer, Unset):
            adresvoorstelling_huisnummer = UNSET
        else:
            adresvoorstelling_huisnummer = AdresvoorstellingAdresvoorstellingHuisnummer.from_dict(
                _adresvoorstelling_huisnummer
            )

        _adresvoorstelling_postcode = d.pop("Adresvoorstelling.postcode", UNSET)
        adresvoorstelling_postcode: AdresvoorstellingAdresvoorstellingPostcode | Unset
        if isinstance(_adresvoorstelling_postcode, Unset):
            adresvoorstelling_postcode = UNSET
        else:
            adresvoorstelling_postcode = AdresvoorstellingAdresvoorstellingPostcode.from_dict(
                _adresvoorstelling_postcode
            )

        _adresvoorstelling_gemeentenaam = d.pop("Adresvoorstelling.gemeentenaam", UNSET)
        adresvoorstelling_gemeentenaam: AdresvoorstellingAdresvoorstellingGemeentenaam | Unset
        if isinstance(_adresvoorstelling_gemeentenaam, Unset):
            adresvoorstelling_gemeentenaam = UNSET
        else:
            adresvoorstelling_gemeentenaam = AdresvoorstellingAdresvoorstellingGemeentenaam.from_dict(
                _adresvoorstelling_gemeentenaam
            )

        _adresvoorstelling_gemeentecode = d.pop("Adresvoorstelling.gemeentecode", UNSET)
        adresvoorstelling_gemeentecode: AdresvoorstellingAdresvoorstellingGemeentecode | Unset
        if isinstance(_adresvoorstelling_gemeentecode, Unset):
            adresvoorstelling_gemeentecode = UNSET
        else:
            adresvoorstelling_gemeentecode = AdresvoorstellingAdresvoorstellingGemeentecode.from_dict(
                _adresvoorstelling_gemeentecode
            )

        _adresvoorstelling_land = d.pop("Adresvoorstelling.land", UNSET)
        adresvoorstelling_land: AdresvoorstellingAdresvoorstellingLand | Unset
        if isinstance(_adresvoorstelling_land, Unset):
            adresvoorstelling_land = UNSET
        else:
            adresvoorstelling_land = AdresvoorstellingAdresvoorstellingLand.from_dict(_adresvoorstelling_land)

        adresvoorstelling = cls(
            type_=type_,
            id=id,
            adresvoorstelling_straatnaam=adresvoorstelling_straatnaam,
            adresvoorstelling_straatcode=adresvoorstelling_straatcode,
            adresvoorstelling_busnummer=adresvoorstelling_busnummer,
            adresvoorstelling_huisnummer=adresvoorstelling_huisnummer,
            adresvoorstelling_postcode=adresvoorstelling_postcode,
            adresvoorstelling_gemeentenaam=adresvoorstelling_gemeentenaam,
            adresvoorstelling_gemeentecode=adresvoorstelling_gemeentecode,
            adresvoorstelling_land=adresvoorstelling_land,
        )

        adresvoorstelling.additional_properties = d
        return adresvoorstelling

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
