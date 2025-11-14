from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactpunt_type import ContactpuntType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactpunt_contactpunt_adres import ContactpuntContactpuntAdres
    from ..models.contactpunt_contactpunt_email import ContactpuntContactpuntEmail
    from ..models.contactpunt_contactpunt_telefoon import ContactpuntContactpuntTelefoon


T = TypeVar("T", bound="Contactpunt")


@_attrs_define
class Contactpunt:
    """Informatie zoals email, telefoon, adres die toelaat om iemand of iets te contacteren.

    Attributes:
        type_ (ContactpuntType): Object type.
        contactpunt_telefoon (ContactpuntContactpuntTelefoon | Unset): Telefoonnummer waarop men kan bellen.
        contactpunt_adres (ContactpuntContactpuntAdres | Unset): Adres dat men kan aanschrijven of bezoeken.
        contactpunt_email (ContactpuntContactpuntEmail | Unset): Email-adres waarnaar men kan mailen.
    """

    type_: ContactpuntType
    contactpunt_telefoon: ContactpuntContactpuntTelefoon | Unset = UNSET
    contactpunt_adres: ContactpuntContactpuntAdres | Unset = UNSET
    contactpunt_email: ContactpuntContactpuntEmail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        contactpunt_telefoon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contactpunt_telefoon, Unset):
            contactpunt_telefoon = self.contactpunt_telefoon.to_dict()

        contactpunt_adres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contactpunt_adres, Unset):
            contactpunt_adres = self.contactpunt_adres.to_dict()

        contactpunt_email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contactpunt_email, Unset):
            contactpunt_email = self.contactpunt_email.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@type": type_,
            }
        )
        if contactpunt_telefoon is not UNSET:
            field_dict["Contactpunt.telefoon"] = contactpunt_telefoon
        if contactpunt_adres is not UNSET:
            field_dict["Contactpunt.adres"] = contactpunt_adres
        if contactpunt_email is not UNSET:
            field_dict["Contactpunt.email"] = contactpunt_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactpunt_contactpunt_adres import ContactpuntContactpuntAdres
        from ..models.contactpunt_contactpunt_email import ContactpuntContactpuntEmail
        from ..models.contactpunt_contactpunt_telefoon import ContactpuntContactpuntTelefoon

        d = dict(src_dict)
        type_ = ContactpuntType(d.pop("@type"))

        _contactpunt_telefoon = d.pop("Contactpunt.telefoon", UNSET)
        contactpunt_telefoon: ContactpuntContactpuntTelefoon | Unset
        if isinstance(_contactpunt_telefoon, Unset):
            contactpunt_telefoon = UNSET
        else:
            contactpunt_telefoon = ContactpuntContactpuntTelefoon.from_dict(_contactpunt_telefoon)

        _contactpunt_adres = d.pop("Contactpunt.adres", UNSET)
        contactpunt_adres: ContactpuntContactpuntAdres | Unset
        if isinstance(_contactpunt_adres, Unset):
            contactpunt_adres = UNSET
        else:
            contactpunt_adres = ContactpuntContactpuntAdres.from_dict(_contactpunt_adres)

        _contactpunt_email = d.pop("Contactpunt.email", UNSET)
        contactpunt_email: ContactpuntContactpuntEmail | Unset
        if isinstance(_contactpunt_email, Unset):
            contactpunt_email = UNSET
        else:
            contactpunt_email = ContactpuntContactpuntEmail.from_dict(_contactpunt_email)

        contactpunt = cls(
            type_=type_,
            contactpunt_telefoon=contactpunt_telefoon,
            contactpunt_adres=contactpunt_adres,
            contactpunt_email=contactpunt_email,
        )

        contactpunt.additional_properties = d
        return contactpunt

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
