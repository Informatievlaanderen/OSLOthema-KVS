from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_ld_root_context_item_type_0 import JsonLdRootContextItemType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activeringstraject import Activeringstraject
    from ..models.adresvoorstelling import Adresvoorstelling
    from ..models.deeltraject import Deeltraject
    from ..models.domicilie import Domicilie
    from ..models.geregistreerd_persoon import GeregistreerdPersoon
    from ..models.geregistreerde_organisatie import GeregistreerdeOrganisatie
    from ..models.json_ld_root_context_item_type_1 import JsonLdRootContextItemType1
    from ..models.participatie import Participatie
    from ..models.persoon import Persoon
    from ..models.publieke_dienstverlening import PubliekeDienstverlening
    from ..models.publieke_organisatie import PubliekeOrganisatie
    from ..models.verblijfplaats import Verblijfplaats
    from ..models.werkvoorkeuren import Werkvoorkeuren


T = TypeVar("T", bound="JsonLdRoot")


@_attrs_define
class JsonLdRoot:
    """
    Attributes:
        context (list[JsonLdRootContextItemType0 | JsonLdRootContextItemType1] | Unset): JSON-LD's context which defines
            how the JSON-LD keys are mapped to URIs.
        graph (list[Activeringstraject | Adresvoorstelling | Deeltraject | Domicilie | GeregistreerdeOrganisatie |
            GeregistreerdPersoon | Participatie | Persoon | PubliekeDienstverlening | PubliekeOrganisatie | Verblijfplaats |
            Werkvoorkeuren] | Unset):
    """

    context: list[JsonLdRootContextItemType0 | JsonLdRootContextItemType1] | Unset = UNSET
    graph: (
        list[
            Activeringstraject
            | Adresvoorstelling
            | Deeltraject
            | Domicilie
            | GeregistreerdeOrganisatie
            | GeregistreerdPersoon
            | Participatie
            | Persoon
            | PubliekeDienstverlening
            | PubliekeOrganisatie
            | Verblijfplaats
            | Werkvoorkeuren
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activeringstraject import Activeringstraject
        from ..models.deeltraject import Deeltraject
        from ..models.domicilie import Domicilie
        from ..models.geregistreerd_persoon import GeregistreerdPersoon
        from ..models.geregistreerde_organisatie import GeregistreerdeOrganisatie
        from ..models.participatie import Participatie
        from ..models.persoon import Persoon
        from ..models.publieke_dienstverlening import PubliekeDienstverlening
        from ..models.publieke_organisatie import PubliekeOrganisatie
        from ..models.verblijfplaats import Verblijfplaats
        from ..models.werkvoorkeuren import Werkvoorkeuren

        context: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = []
            for context_item_data in self.context:
                context_item: dict[str, Any] | str
                if isinstance(context_item_data, JsonLdRootContextItemType0):
                    context_item = context_item_data.value
                else:
                    context_item = context_item_data.to_dict()

                context.append(context_item)

        graph: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.graph, Unset):
            graph = []
            for graph_item_data in self.graph:
                graph_item: dict[str, Any]
                if isinstance(graph_item_data, Werkvoorkeuren):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, GeregistreerdPersoon):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, Persoon):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, PubliekeOrganisatie):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, GeregistreerdeOrganisatie):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, Participatie):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, PubliekeDienstverlening):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, Activeringstraject):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, Deeltraject):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, Verblijfplaats):
                    graph_item = graph_item_data.to_dict()
                elif isinstance(graph_item_data, Domicilie):
                    graph_item = graph_item_data.to_dict()
                else:
                    graph_item = graph_item_data.to_dict()

                graph.append(graph_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["@context"] = context
        if graph is not UNSET:
            field_dict["@graph"] = graph

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activeringstraject import Activeringstraject
        from ..models.adresvoorstelling import Adresvoorstelling
        from ..models.deeltraject import Deeltraject
        from ..models.domicilie import Domicilie
        from ..models.geregistreerd_persoon import GeregistreerdPersoon
        from ..models.geregistreerde_organisatie import GeregistreerdeOrganisatie
        from ..models.json_ld_root_context_item_type_1 import JsonLdRootContextItemType1
        from ..models.participatie import Participatie
        from ..models.persoon import Persoon
        from ..models.publieke_dienstverlening import PubliekeDienstverlening
        from ..models.publieke_organisatie import PubliekeOrganisatie
        from ..models.verblijfplaats import Verblijfplaats
        from ..models.werkvoorkeuren import Werkvoorkeuren

        d = dict(src_dict)
        _context = d.pop("@context", UNSET)
        context: list[JsonLdRootContextItemType0 | JsonLdRootContextItemType1] | Unset = UNSET
        if _context is not UNSET:
            context = []
            for context_item_data in _context:

                def _parse_context_item(data: object) -> JsonLdRootContextItemType0 | JsonLdRootContextItemType1:
                    try:
                        if not isinstance(data, str):
                            raise TypeError()
                        context_item_type_0 = JsonLdRootContextItemType0(data)

                        return context_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    context_item_type_1 = JsonLdRootContextItemType1.from_dict(data)

                    return context_item_type_1

                context_item = _parse_context_item(context_item_data)

                context.append(context_item)

        _graph = d.pop("@graph", UNSET)
        graph: (
            list[
                Activeringstraject
                | Adresvoorstelling
                | Deeltraject
                | Domicilie
                | GeregistreerdeOrganisatie
                | GeregistreerdPersoon
                | Participatie
                | Persoon
                | PubliekeDienstverlening
                | PubliekeOrganisatie
                | Verblijfplaats
                | Werkvoorkeuren
            ]
            | Unset
        ) = UNSET
        if _graph is not UNSET:
            graph = []
            for graph_item_data in _graph:

                def _parse_graph_item(
                    data: object,
                ) -> (
                    Activeringstraject
                    | Adresvoorstelling
                    | Deeltraject
                    | Domicilie
                    | GeregistreerdeOrganisatie
                    | GeregistreerdPersoon
                    | Participatie
                    | Persoon
                    | PubliekeDienstverlening
                    | PubliekeOrganisatie
                    | Verblijfplaats
                    | Werkvoorkeuren
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_0 = Werkvoorkeuren.from_dict(data)

                        return graph_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_1 = GeregistreerdPersoon.from_dict(data)

                        return graph_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_2 = Persoon.from_dict(data)

                        return graph_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_3 = PubliekeOrganisatie.from_dict(data)

                        return graph_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_4 = GeregistreerdeOrganisatie.from_dict(data)

                        return graph_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_5 = Participatie.from_dict(data)

                        return graph_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_6 = PubliekeDienstverlening.from_dict(data)

                        return graph_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_7 = Activeringstraject.from_dict(data)

                        return graph_item_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_8 = Deeltraject.from_dict(data)

                        return graph_item_type_8
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_9 = Verblijfplaats.from_dict(data)

                        return graph_item_type_9
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        graph_item_type_10 = Domicilie.from_dict(data)

                        return graph_item_type_10
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    graph_item_type_11 = Adresvoorstelling.from_dict(data)

                    return graph_item_type_11

                graph_item = _parse_graph_item(graph_item_data)

                graph.append(graph_item)

        json_ld_root = cls(
            context=context,
            graph=graph,
        )

        json_ld_root.additional_properties = d
        return json_ld_root

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
