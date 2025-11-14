from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.participatie_type import ParticipatieType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participatie_participatie_heeft_participant import ParticipatieParticipatieHeeftParticipant
    from ..models.participatie_participatie_rol import ParticipatieParticipatieRol


T = TypeVar("T", bound="Participatie")


@_attrs_define
class Participatie:
    """De rol waarin een Agent deelneemt aan de Publieke Dienstverlening.

    Attributes:
        id (str): Object ID. Can be an URI or internal reference such as _:MyID.
        type_ (ParticipatieType): Object type.
        participatie_rol (ParticipatieParticipatieRol | Unset): De functie van de Agent bij het deelnemen.
        participatie_heeft_participant (ParticipatieParticipatieHeeftParticipant | Unset): De Agenten die deelnemen.
    """

    id: str
    type_: ParticipatieType
    participatie_rol: ParticipatieParticipatieRol | Unset = UNSET
    participatie_heeft_participant: ParticipatieParticipatieHeeftParticipant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        participatie_rol: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participatie_rol, Unset):
            participatie_rol = self.participatie_rol.to_dict()

        participatie_heeft_participant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participatie_heeft_participant, Unset):
            participatie_heeft_participant = self.participatie_heeft_participant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
            }
        )
        if participatie_rol is not UNSET:
            field_dict["Participatie.rol"] = participatie_rol
        if participatie_heeft_participant is not UNSET:
            field_dict["Participatie.heeftParticipant"] = participatie_heeft_participant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participatie_participatie_heeft_participant import ParticipatieParticipatieHeeftParticipant
        from ..models.participatie_participatie_rol import ParticipatieParticipatieRol

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = ParticipatieType(d.pop("@type"))

        _participatie_rol = d.pop("Participatie.rol", UNSET)
        participatie_rol: ParticipatieParticipatieRol | Unset
        if isinstance(_participatie_rol, Unset):
            participatie_rol = UNSET
        else:
            participatie_rol = ParticipatieParticipatieRol.from_dict(_participatie_rol)

        _participatie_heeft_participant = d.pop("Participatie.heeftParticipant", UNSET)
        participatie_heeft_participant: ParticipatieParticipatieHeeftParticipant | Unset
        if isinstance(_participatie_heeft_participant, Unset):
            participatie_heeft_participant = UNSET
        else:
            participatie_heeft_participant = ParticipatieParticipatieHeeftParticipant.from_dict(
                _participatie_heeft_participant
            )

        participatie = cls(
            id=id,
            type_=type_,
            participatie_rol=participatie_rol,
            participatie_heeft_participant=participatie_heeft_participant,
        )

        participatie.additional_properties = d
        return participatie

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
