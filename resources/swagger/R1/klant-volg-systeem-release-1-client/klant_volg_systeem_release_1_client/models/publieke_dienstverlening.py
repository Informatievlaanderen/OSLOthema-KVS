from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publieke_dienstverlening_type import PubliekeDienstverleningType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.publieke_dienstverlening_publieke_dienstverlening_finaliteit import (
        PubliekeDienstverleningPubliekeDienstverleningFinaliteit,
    )
    from ..models.publieke_dienstverlening_publieke_dienstverlening_gebruikt_item import (
        PubliekeDienstverleningPubliekeDienstverleningGebruiktItem,
    )
    from ..models.publieke_dienstverlening_publieke_dienstverlening_heeft_participatie_item import (
        PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieItem,
    )
    from ..models.publieke_dienstverlening_publieke_dienstverlening_heeft_verantwoordelijke import (
        PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke,
    )
    from ..models.publieke_dienstverlening_publieke_dienstverlening_naam import (
        PubliekeDienstverleningPubliekeDienstverleningNaam,
    )
    from ..models.publieke_dienstverlening_publieke_dienstverlening_produceert_item import (
        PubliekeDienstverleningPubliekeDienstverleningProduceertItem,
    )
    from ..models.publieke_dienstverlening_publieke_dienstverlening_type import (
        PubliekeDienstverleningPubliekeDienstverleningType,
    )


T = TypeVar("T", bound="PubliekeDienstverlening")


@_attrs_define
class PubliekeDienstverlening:
    """Een publieke dienstverlening is een geheel van verplichte of optioneel uitgevoerde of uitvoerbare acties door of in
    naam van een publieke organisatie. De dienstverlening is ten bate van een individu, een bedrijf, een andere publieke
    organisatie of groepen.

        Attributes:
            id (str): Object ID. Can be an URI or internal reference such as _:MyID.
            type_ (PubliekeDienstverleningType): Object type.
            publieke_dienstverlening_naam (PubliekeDienstverleningPubliekeDienstverleningNaam): De naam van de Publieke
                Dienstverlening.
            publieke_dienstverlening_heeft_verantwoordelijke
                (PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke): De Publieke Organisatie die
                verantwoordelijk is voor de Publieke Dienstverlening.
            publieke_dienstverlening_heeft_participatie
                (list[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieItem] | Unset): De Agenten die deelnemen
                aan de Publieke Dienstverlening.
            publieke_dienstverlening_gebruikt (list[PubliekeDienstverleningPubliekeDienstverleningGebruiktItem] | Unset):
                Referenties naar alle Inputs die de Publieke Dienstverlening gebruikt om een of meerdere Outputs te produceren.
            publieke_dienstverlening_produceert (list[PubliekeDienstverleningPubliekeDienstverleningProduceertItem] |
                Unset): De referenties naar alle resources die de Publieke Dienstverlening produceert.
            publieke_dienstverlening_type (PubliekeDienstverleningPubliekeDienstverleningType | Unset): Het soort Publieke
                Dienstverlening.
            publieke_dienstverlening_finaliteit (PubliekeDienstverleningPubliekeDienstverleningFinaliteit | Unset):
                Wettelijk kader waarvoor de informatie wordt bevraagd.
    """

    id: str
    type_: PubliekeDienstverleningType
    publieke_dienstverlening_naam: PubliekeDienstverleningPubliekeDienstverleningNaam
    publieke_dienstverlening_heeft_verantwoordelijke: (
        PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke
    )
    publieke_dienstverlening_heeft_participatie: (
        list[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieItem] | Unset
    ) = UNSET
    publieke_dienstverlening_gebruikt: list[PubliekeDienstverleningPubliekeDienstverleningGebruiktItem] | Unset = UNSET
    publieke_dienstverlening_produceert: list[PubliekeDienstverleningPubliekeDienstverleningProduceertItem] | Unset = (
        UNSET
    )
    publieke_dienstverlening_type: PubliekeDienstverleningPubliekeDienstverleningType | Unset = UNSET
    publieke_dienstverlening_finaliteit: PubliekeDienstverleningPubliekeDienstverleningFinaliteit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        publieke_dienstverlening_naam = self.publieke_dienstverlening_naam.to_dict()

        publieke_dienstverlening_heeft_verantwoordelijke = (
            self.publieke_dienstverlening_heeft_verantwoordelijke.to_dict()
        )

        publieke_dienstverlening_heeft_participatie: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publieke_dienstverlening_heeft_participatie, Unset):
            publieke_dienstverlening_heeft_participatie = []
            for (
                publieke_dienstverlening_heeft_participatie_item_data
            ) in self.publieke_dienstverlening_heeft_participatie:
                publieke_dienstverlening_heeft_participatie_item = (
                    publieke_dienstverlening_heeft_participatie_item_data.to_dict()
                )
                publieke_dienstverlening_heeft_participatie.append(publieke_dienstverlening_heeft_participatie_item)

        publieke_dienstverlening_gebruikt: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publieke_dienstverlening_gebruikt, Unset):
            publieke_dienstverlening_gebruikt = []
            for publieke_dienstverlening_gebruikt_item_data in self.publieke_dienstverlening_gebruikt:
                publieke_dienstverlening_gebruikt_item = publieke_dienstverlening_gebruikt_item_data.to_dict()
                publieke_dienstverlening_gebruikt.append(publieke_dienstverlening_gebruikt_item)

        publieke_dienstverlening_produceert: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publieke_dienstverlening_produceert, Unset):
            publieke_dienstverlening_produceert = []
            for publieke_dienstverlening_produceert_item_data in self.publieke_dienstverlening_produceert:
                publieke_dienstverlening_produceert_item = publieke_dienstverlening_produceert_item_data.to_dict()
                publieke_dienstverlening_produceert.append(publieke_dienstverlening_produceert_item)

        publieke_dienstverlening_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publieke_dienstverlening_type, Unset):
            publieke_dienstverlening_type = self.publieke_dienstverlening_type.to_dict()

        publieke_dienstverlening_finaliteit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publieke_dienstverlening_finaliteit, Unset):
            publieke_dienstverlening_finaliteit = self.publieke_dienstverlening_finaliteit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@id": id,
                "@type": type_,
                "PubliekeDienstverlening.naam": publieke_dienstverlening_naam,
                "PubliekeDienstverlening.heeftVerantwoordelijke": publieke_dienstverlening_heeft_verantwoordelijke,
            }
        )
        if publieke_dienstverlening_heeft_participatie is not UNSET:
            field_dict["PubliekeDienstverlening.heeftParticipatie"] = publieke_dienstverlening_heeft_participatie
        if publieke_dienstverlening_gebruikt is not UNSET:
            field_dict["PubliekeDienstverlening.gebruikt"] = publieke_dienstverlening_gebruikt
        if publieke_dienstverlening_produceert is not UNSET:
            field_dict["PubliekeDienstverlening.produceert"] = publieke_dienstverlening_produceert
        if publieke_dienstverlening_type is not UNSET:
            field_dict["PubliekeDienstverlening.type"] = publieke_dienstverlening_type
        if publieke_dienstverlening_finaliteit is not UNSET:
            field_dict["PubliekeDienstverlening.finaliteit"] = publieke_dienstverlening_finaliteit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publieke_dienstverlening_publieke_dienstverlening_finaliteit import (
            PubliekeDienstverleningPubliekeDienstverleningFinaliteit,
        )
        from ..models.publieke_dienstverlening_publieke_dienstverlening_gebruikt_item import (
            PubliekeDienstverleningPubliekeDienstverleningGebruiktItem,
        )
        from ..models.publieke_dienstverlening_publieke_dienstverlening_heeft_participatie_item import (
            PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieItem,
        )
        from ..models.publieke_dienstverlening_publieke_dienstverlening_heeft_verantwoordelijke import (
            PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke,
        )
        from ..models.publieke_dienstverlening_publieke_dienstverlening_naam import (
            PubliekeDienstverleningPubliekeDienstverleningNaam,
        )
        from ..models.publieke_dienstverlening_publieke_dienstverlening_produceert_item import (
            PubliekeDienstverleningPubliekeDienstverleningProduceertItem,
        )
        from ..models.publieke_dienstverlening_publieke_dienstverlening_type import (
            PubliekeDienstverleningPubliekeDienstverleningType,
        )

        d = dict(src_dict)
        id = d.pop("@id")

        type_ = PubliekeDienstverleningType(d.pop("@type"))

        publieke_dienstverlening_naam = PubliekeDienstverleningPubliekeDienstverleningNaam.from_dict(
            d.pop("PubliekeDienstverlening.naam")
        )

        publieke_dienstverlening_heeft_verantwoordelijke = (
            PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke.from_dict(
                d.pop("PubliekeDienstverlening.heeftVerantwoordelijke")
            )
        )

        _publieke_dienstverlening_heeft_participatie = d.pop("PubliekeDienstverlening.heeftParticipatie", UNSET)
        publieke_dienstverlening_heeft_participatie: (
            list[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieItem] | Unset
        ) = UNSET
        if _publieke_dienstverlening_heeft_participatie is not UNSET:
            publieke_dienstverlening_heeft_participatie = []
            for publieke_dienstverlening_heeft_participatie_item_data in _publieke_dienstverlening_heeft_participatie:
                publieke_dienstverlening_heeft_participatie_item = (
                    PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieItem.from_dict(
                        publieke_dienstverlening_heeft_participatie_item_data
                    )
                )

                publieke_dienstverlening_heeft_participatie.append(publieke_dienstverlening_heeft_participatie_item)

        _publieke_dienstverlening_gebruikt = d.pop("PubliekeDienstverlening.gebruikt", UNSET)
        publieke_dienstverlening_gebruikt: list[PubliekeDienstverleningPubliekeDienstverleningGebruiktItem] | Unset = (
            UNSET
        )
        if _publieke_dienstverlening_gebruikt is not UNSET:
            publieke_dienstverlening_gebruikt = []
            for publieke_dienstverlening_gebruikt_item_data in _publieke_dienstverlening_gebruikt:
                publieke_dienstverlening_gebruikt_item = (
                    PubliekeDienstverleningPubliekeDienstverleningGebruiktItem.from_dict(
                        publieke_dienstverlening_gebruikt_item_data
                    )
                )

                publieke_dienstverlening_gebruikt.append(publieke_dienstverlening_gebruikt_item)

        _publieke_dienstverlening_produceert = d.pop("PubliekeDienstverlening.produceert", UNSET)
        publieke_dienstverlening_produceert: (
            list[PubliekeDienstverleningPubliekeDienstverleningProduceertItem] | Unset
        ) = UNSET
        if _publieke_dienstverlening_produceert is not UNSET:
            publieke_dienstverlening_produceert = []
            for publieke_dienstverlening_produceert_item_data in _publieke_dienstverlening_produceert:
                publieke_dienstverlening_produceert_item = (
                    PubliekeDienstverleningPubliekeDienstverleningProduceertItem.from_dict(
                        publieke_dienstverlening_produceert_item_data
                    )
                )

                publieke_dienstverlening_produceert.append(publieke_dienstverlening_produceert_item)

        _publieke_dienstverlening_type = d.pop("PubliekeDienstverlening.type", UNSET)
        publieke_dienstverlening_type: PubliekeDienstverleningPubliekeDienstverleningType | Unset
        if isinstance(_publieke_dienstverlening_type, Unset):
            publieke_dienstverlening_type = UNSET
        else:
            publieke_dienstverlening_type = PubliekeDienstverleningPubliekeDienstverleningType.from_dict(
                _publieke_dienstverlening_type
            )

        _publieke_dienstverlening_finaliteit = d.pop("PubliekeDienstverlening.finaliteit", UNSET)
        publieke_dienstverlening_finaliteit: PubliekeDienstverleningPubliekeDienstverleningFinaliteit | Unset
        if isinstance(_publieke_dienstverlening_finaliteit, Unset):
            publieke_dienstverlening_finaliteit = UNSET
        else:
            publieke_dienstverlening_finaliteit = PubliekeDienstverleningPubliekeDienstverleningFinaliteit.from_dict(
                _publieke_dienstverlening_finaliteit
            )

        publieke_dienstverlening = cls(
            id=id,
            type_=type_,
            publieke_dienstverlening_naam=publieke_dienstverlening_naam,
            publieke_dienstverlening_heeft_verantwoordelijke=publieke_dienstverlening_heeft_verantwoordelijke,
            publieke_dienstverlening_heeft_participatie=publieke_dienstverlening_heeft_participatie,
            publieke_dienstverlening_gebruikt=publieke_dienstverlening_gebruikt,
            publieke_dienstverlening_produceert=publieke_dienstverlening_produceert,
            publieke_dienstverlening_type=publieke_dienstverlening_type,
            publieke_dienstverlening_finaliteit=publieke_dienstverlening_finaliteit,
        )

        publieke_dienstverlening.additional_properties = d
        return publieke_dienstverlening

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
