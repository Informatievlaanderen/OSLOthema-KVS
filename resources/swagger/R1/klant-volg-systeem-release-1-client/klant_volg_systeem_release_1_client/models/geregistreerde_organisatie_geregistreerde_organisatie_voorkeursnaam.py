from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geregistreerde_organisatie_geregistreerde_organisatie_voorkeursnaam_language import (
    GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaamLanguage,
)

T = TypeVar("T", bound="GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam")


@_attrs_define
class GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam:
    """Naam waarmee de Organisatie bij voorkeur wordt aangeduid

    Attributes:
        value (str): JSON-LD's Literal string value.
        language (GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaamLanguage): The language in which the
            Literal string is written.
    """

    value: str
    language: GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaamLanguage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        language = self.language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@value": value,
                "@language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("@value")

        language = GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaamLanguage(d.pop("@language"))

        geregistreerde_organisatie_geregistreerde_organisatie_voorkeursnaam = cls(
            value=value,
            language=language,
        )

        geregistreerde_organisatie_geregistreerde_organisatie_voorkeursnaam.additional_properties = d
        return geregistreerde_organisatie_geregistreerde_organisatie_voorkeursnaam

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
