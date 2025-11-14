from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deeltraject_type import DeeltrajectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deeltraject_deeltraject_einddatum import DeeltrajectDeeltrajectEinddatum
    from ..models.deeltraject_deeltraject_heeft_participatie_item import DeeltrajectDeeltrajectHeeftParticipatieItem
    from ..models.deeltraject_deeltraject_naam import DeeltrajectDeeltrajectNaam
    from ..models.deeltraject_deeltraject_startdatum import DeeltrajectDeeltrajectStartdatum
    from ..models.deeltraject_deeltraject_status import DeeltrajectDeeltrajectStatus
    from ..models.deeltraject_deeltraject_type import DeeltrajectDeeltrajectType


T = TypeVar("T", bound="Deeltraject")


@_attrs_define
class Deeltraject:
    """
    Attributes:
        id (str): Object ID. Can be an URI or internal reference such as _:MyID.
        type_ (DeeltrajectType): Object type.
        deeltraject_naam (DeeltrajectDeeltrajectNaam | Unset): De naam van een Deeltraject.
        deeltraject_startdatum (DeeltrajectDeeltrajectStartdatum | Unset): De datum waarop het Deeltraject start.
        deeltraject_einddatum (DeeltrajectDeeltrajectEinddatum | Unset): De datum waarop het Deeltraject eindigt.
        deeltraject_type (DeeltrajectDeeltrajectType | Unset):
        deeltraject_status (DeeltrajectDeeltrajectStatus | Unset):
        deeltraject_heeft_participatie (list[DeeltrajectDeeltrajectHeeftParticipatieItem] | Unset):
    """

    id: str
    type_: DeeltrajectType
    deeltraject_naam: DeeltrajectDeeltrajectNaam | Unset = UNSET
    deeltraject_startdatum: DeeltrajectDeeltrajectStartdatum | Unset = UNSET
    deeltraject_einddatum: DeeltrajectDeeltrajectEinddatum | Unset = UNSET
    deeltraject_type: DeeltrajectDeeltrajectType | Unset = UNSET
    deeltraject_status: DeeltrajectDeeltrajectStatus | Unset = UNSET
    deeltraject_heeft_participatie: list[DeeltrajectDeeltrajectHeeftParticipatieItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        deeltraject_naam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deeltraject_naam, Unset):
            deeltraject_naam = self.deeltraject_naam.to_dict()

        deeltraject_startdatum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deeltraject_startdatum, Unset):
            deeltraject_startdatum = self.deeltraject_startdatum.to_dict()

        deeltraject_einddatum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deeltraject_einddatum, Unset):
            deeltraject_einddatum = self.deeltraject_einddatum.to_dict()

        deeltraject_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deeltraject_type, Unset):
            deeltraject_type = self.deeltraject_type.to_dict()

        deeltraject_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deeltraject_status, Unset):
            deeltraject_status = self.deeltraject_status.to_dict()

        deeltraject_heeft_participatie: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deeltraject_heeft_participatie, Unset):
            deeltraject_heeft_participatie = []
            for deeltraject_heeft_participatie_item_data in self.deeltraject_heeft_participatie:
                deeltraject_heeft_participatie_item = deeltraject_heeft_participatie_item_data.to_dict()
                deeltraject_heeft_participatie.append(deeltraject_heeft_participatie_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
            }
        )
        if deeltraject_naam is not UNSET:
            field_dict["Deeltraject.naam"] = deeltraject_naam
        if deeltraject_startdatum is not UNSET:
            field_dict["Deeltraject.startdatum"] = deeltraject_startdatum
        if deeltraject_einddatum is not UNSET:
            field_dict["Deeltraject.einddatum"] = deeltraject_einddatum
        if deeltraject_type is not UNSET:
            field_dict["Deeltraject.type"] = deeltraject_type
        if deeltraject_status is not UNSET:
            field_dict["Deeltraject.status"] = deeltraject_status
        if deeltraject_heeft_participatie is not UNSET:
            field_dict["Deeltraject.heeftParticipatie"] = deeltraject_heeft_participatie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deeltraject_deeltraject_einddatum import DeeltrajectDeeltrajectEinddatum
        from ..models.deeltraject_deeltraject_heeft_participatie_item import DeeltrajectDeeltrajectHeeftParticipatieItem
        from ..models.deeltraject_deeltraject_naam import DeeltrajectDeeltrajectNaam
        from ..models.deeltraject_deeltraject_startdatum import DeeltrajectDeeltrajectStartdatum
        from ..models.deeltraject_deeltraject_status import DeeltrajectDeeltrajectStatus
        from ..models.deeltraject_deeltraject_type import DeeltrajectDeeltrajectType

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = DeeltrajectType(d.pop("@type"))

        _deeltraject_naam = d.pop("Deeltraject.naam", UNSET)
        deeltraject_naam: DeeltrajectDeeltrajectNaam | Unset
        if isinstance(_deeltraject_naam, Unset):
            deeltraject_naam = UNSET
        else:
            deeltraject_naam = DeeltrajectDeeltrajectNaam.from_dict(_deeltraject_naam)

        _deeltraject_startdatum = d.pop("Deeltraject.startdatum", UNSET)
        deeltraject_startdatum: DeeltrajectDeeltrajectStartdatum | Unset
        if isinstance(_deeltraject_startdatum, Unset):
            deeltraject_startdatum = UNSET
        else:
            deeltraject_startdatum = DeeltrajectDeeltrajectStartdatum.from_dict(_deeltraject_startdatum)

        _deeltraject_einddatum = d.pop("Deeltraject.einddatum", UNSET)
        deeltraject_einddatum: DeeltrajectDeeltrajectEinddatum | Unset
        if isinstance(_deeltraject_einddatum, Unset):
            deeltraject_einddatum = UNSET
        else:
            deeltraject_einddatum = DeeltrajectDeeltrajectEinddatum.from_dict(_deeltraject_einddatum)

        _deeltraject_type = d.pop("Deeltraject.type", UNSET)
        deeltraject_type: DeeltrajectDeeltrajectType | Unset
        if isinstance(_deeltraject_type, Unset):
            deeltraject_type = UNSET
        else:
            deeltraject_type = DeeltrajectDeeltrajectType.from_dict(_deeltraject_type)

        _deeltraject_status = d.pop("Deeltraject.status", UNSET)
        deeltraject_status: DeeltrajectDeeltrajectStatus | Unset
        if isinstance(_deeltraject_status, Unset):
            deeltraject_status = UNSET
        else:
            deeltraject_status = DeeltrajectDeeltrajectStatus.from_dict(_deeltraject_status)

        _deeltraject_heeft_participatie = d.pop("Deeltraject.heeftParticipatie", UNSET)
        deeltraject_heeft_participatie: list[DeeltrajectDeeltrajectHeeftParticipatieItem] | Unset = UNSET
        if _deeltraject_heeft_participatie is not UNSET:
            deeltraject_heeft_participatie = []
            for deeltraject_heeft_participatie_item_data in _deeltraject_heeft_participatie:
                deeltraject_heeft_participatie_item = DeeltrajectDeeltrajectHeeftParticipatieItem.from_dict(
                    deeltraject_heeft_participatie_item_data
                )

                deeltraject_heeft_participatie.append(deeltraject_heeft_participatie_item)

        deeltraject = cls(
            id=id,
            type_=type_,
            deeltraject_naam=deeltraject_naam,
            deeltraject_startdatum=deeltraject_startdatum,
            deeltraject_einddatum=deeltraject_einddatum,
            deeltraject_type=deeltraject_type,
            deeltraject_status=deeltraject_status,
            deeltraject_heeft_participatie=deeltraject_heeft_participatie,
        )

        deeltraject.additional_properties = d
        return deeltraject

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
