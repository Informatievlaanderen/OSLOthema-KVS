from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activeringstraject_type import ActiveringstrajectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activeringstraject_activeringstraject_einddatum import ActiveringstrajectActiveringstrajectEinddatum
    from ..models.activeringstraject_activeringstraject_heeft_participatie_item import (
        ActiveringstrajectActiveringstrajectHeeftParticipatieItem,
    )
    from ..models.activeringstraject_activeringstraject_naam import ActiveringstrajectActiveringstrajectNaam
    from ..models.activeringstraject_activeringstraject_startdatum import ActiveringstrajectActiveringstrajectStartdatum
    from ..models.activeringstraject_activeringstraject_status import ActiveringstrajectActiveringstrajectStatus
    from ..models.deeltraject import Deeltraject


T = TypeVar("T", bound="Activeringstraject")


@_attrs_define
class Activeringstraject:
    """Een Activeringstraject is een specifiekere variant van een Traject dat moet aansporen om de Werkzoekende te
    activeren naar werk.

        Attributes:
            id (str): Object ID. Can be an URI or internal reference such as _:MyID.
            type_ (ActiveringstrajectType): Object type.
            activeringstraject_naam (ActiveringstrajectActiveringstrajectNaam): De naam van een Traject.
            activeringstraject_startdatum (ActiveringstrajectActiveringstrajectStartdatum | Unset): De datum waarop het
                Traject start.
            activeringstraject_einddatum (ActiveringstrajectActiveringstrajectEinddatum | Unset): De datum waarop het
                Traject eindigt.
            activeringstraject_status (ActiveringstrajectActiveringstrajectStatus | Unset):
            activeringstraject_deeltraject (list[Deeltraject] | Unset): De Deeltrajecten gelinkt aan dit Traject.
            activeringstraject_heeft_participatie (list[ActiveringstrajectActiveringstrajectHeeftParticipatieItem] | Unset):
    """

    id: str
    type_: ActiveringstrajectType
    activeringstraject_naam: ActiveringstrajectActiveringstrajectNaam
    activeringstraject_startdatum: ActiveringstrajectActiveringstrajectStartdatum | Unset = UNSET
    activeringstraject_einddatum: ActiveringstrajectActiveringstrajectEinddatum | Unset = UNSET
    activeringstraject_status: ActiveringstrajectActiveringstrajectStatus | Unset = UNSET
    activeringstraject_deeltraject: list[Deeltraject] | Unset = UNSET
    activeringstraject_heeft_participatie: list[ActiveringstrajectActiveringstrajectHeeftParticipatieItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        activeringstraject_naam = self.activeringstraject_naam.to_dict()

        activeringstraject_startdatum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activeringstraject_startdatum, Unset):
            activeringstraject_startdatum = self.activeringstraject_startdatum.to_dict()

        activeringstraject_einddatum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activeringstraject_einddatum, Unset):
            activeringstraject_einddatum = self.activeringstraject_einddatum.to_dict()

        activeringstraject_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activeringstraject_status, Unset):
            activeringstraject_status = self.activeringstraject_status.to_dict()

        activeringstraject_deeltraject: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activeringstraject_deeltraject, Unset):
            activeringstraject_deeltraject = []
            for activeringstraject_deeltraject_item_data in self.activeringstraject_deeltraject:
                activeringstraject_deeltraject_item = activeringstraject_deeltraject_item_data.to_dict()
                activeringstraject_deeltraject.append(activeringstraject_deeltraject_item)

        activeringstraject_heeft_participatie: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activeringstraject_heeft_participatie, Unset):
            activeringstraject_heeft_participatie = []
            for activeringstraject_heeft_participatie_item_data in self.activeringstraject_heeft_participatie:
                activeringstraject_heeft_participatie_item = activeringstraject_heeft_participatie_item_data.to_dict()
                activeringstraject_heeft_participatie.append(activeringstraject_heeft_participatie_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
                "Activeringstraject.naam": activeringstraject_naam,
            }
        )
        if activeringstraject_startdatum is not UNSET:
            field_dict["Activeringstraject.startdatum"] = activeringstraject_startdatum
        if activeringstraject_einddatum is not UNSET:
            field_dict["Activeringstraject.einddatum"] = activeringstraject_einddatum
        if activeringstraject_status is not UNSET:
            field_dict["Activeringstraject.status"] = activeringstraject_status
        if activeringstraject_deeltraject is not UNSET:
            field_dict["Activeringstraject.deeltraject"] = activeringstraject_deeltraject
        if activeringstraject_heeft_participatie is not UNSET:
            field_dict["Activeringstraject.heeftParticipatie"] = activeringstraject_heeft_participatie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activeringstraject_activeringstraject_einddatum import (
            ActiveringstrajectActiveringstrajectEinddatum,
        )
        from ..models.activeringstraject_activeringstraject_heeft_participatie_item import (
            ActiveringstrajectActiveringstrajectHeeftParticipatieItem,
        )
        from ..models.activeringstraject_activeringstraject_naam import ActiveringstrajectActiveringstrajectNaam
        from ..models.activeringstraject_activeringstraject_startdatum import (
            ActiveringstrajectActiveringstrajectStartdatum,
        )
        from ..models.activeringstraject_activeringstraject_status import ActiveringstrajectActiveringstrajectStatus
        from ..models.deeltraject import Deeltraject

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = ActiveringstrajectType(d.pop("@type"))

        activeringstraject_naam = ActiveringstrajectActiveringstrajectNaam.from_dict(d.pop("Activeringstraject.naam"))

        _activeringstraject_startdatum = d.pop("Activeringstraject.startdatum", UNSET)
        activeringstraject_startdatum: ActiveringstrajectActiveringstrajectStartdatum | Unset
        if isinstance(_activeringstraject_startdatum, Unset):
            activeringstraject_startdatum = UNSET
        else:
            activeringstraject_startdatum = ActiveringstrajectActiveringstrajectStartdatum.from_dict(
                _activeringstraject_startdatum
            )

        _activeringstraject_einddatum = d.pop("Activeringstraject.einddatum", UNSET)
        activeringstraject_einddatum: ActiveringstrajectActiveringstrajectEinddatum | Unset
        if isinstance(_activeringstraject_einddatum, Unset):
            activeringstraject_einddatum = UNSET
        else:
            activeringstraject_einddatum = ActiveringstrajectActiveringstrajectEinddatum.from_dict(
                _activeringstraject_einddatum
            )

        _activeringstraject_status = d.pop("Activeringstraject.status", UNSET)
        activeringstraject_status: ActiveringstrajectActiveringstrajectStatus | Unset
        if isinstance(_activeringstraject_status, Unset):
            activeringstraject_status = UNSET
        else:
            activeringstraject_status = ActiveringstrajectActiveringstrajectStatus.from_dict(_activeringstraject_status)

        _activeringstraject_deeltraject = d.pop("Activeringstraject.deeltraject", UNSET)
        activeringstraject_deeltraject: list[Deeltraject] | Unset = UNSET
        if _activeringstraject_deeltraject is not UNSET:
            activeringstraject_deeltraject = []
            for activeringstraject_deeltraject_item_data in _activeringstraject_deeltraject:
                activeringstraject_deeltraject_item = Deeltraject.from_dict(activeringstraject_deeltraject_item_data)

                activeringstraject_deeltraject.append(activeringstraject_deeltraject_item)

        _activeringstraject_heeft_participatie = d.pop("Activeringstraject.heeftParticipatie", UNSET)
        activeringstraject_heeft_participatie: (
            list[ActiveringstrajectActiveringstrajectHeeftParticipatieItem] | Unset
        ) = UNSET
        if _activeringstraject_heeft_participatie is not UNSET:
            activeringstraject_heeft_participatie = []
            for activeringstraject_heeft_participatie_item_data in _activeringstraject_heeft_participatie:
                activeringstraject_heeft_participatie_item = (
                    ActiveringstrajectActiveringstrajectHeeftParticipatieItem.from_dict(
                        activeringstraject_heeft_participatie_item_data
                    )
                )

                activeringstraject_heeft_participatie.append(activeringstraject_heeft_participatie_item)

        activeringstraject = cls(
            id=id,
            type_=type_,
            activeringstraject_naam=activeringstraject_naam,
            activeringstraject_startdatum=activeringstraject_startdatum,
            activeringstraject_einddatum=activeringstraject_einddatum,
            activeringstraject_status=activeringstraject_status,
            activeringstraject_deeltraject=activeringstraject_deeltraject,
            activeringstraject_heeft_participatie=activeringstraject_heeft_participatie,
        )

        activeringstraject.additional_properties = d
        return activeringstraject

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
