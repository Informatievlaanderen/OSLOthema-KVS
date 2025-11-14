# JsonLdRootGraphInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**werkvoorkeuren_beroep** | [**List[Beroepstoestand]**](Beroepstoestand.md) | Voorkeuren voor bepaalde beroepen. | [optional] 
**geregistreerd_persoon_registratie** | [**List[Identificator]**](Identificator.md) | Identificatiecode van de persoon in het register. | 
**geregistreerd_persoon_voornaam** | **str** | Naam die een Persoon bij geboorte wordt gegeven. Onderscheidt de Persoon van de andere personen in de familie. | [optional] 
**geregistreerd_persoon_achternaam** | **str** | Gedeelte van de volledige naam van de Persoon ontvangen van de vorige generatie. | [optional] 
**geregistreerd_persoon_werkvoorkeuren** | [**List[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner]**](GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner.md) | De voorkeuren voor werk van een Persoon. | [optional] 
**geregistreerd_persoon_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Persoon te contacteren. | [optional] 
**geregistreerd_persoon_inwonerschap** | [**List[Inwonerschap]**](Inwonerschap.md) | Jurisdictie waarbinnen het Inwonerschap van de Persoon is gedefinieerd. | [optional] 
**persoon_voornaam** | **str** | Naam die een Persoon bij geboorte wordt gegeven. Onderscheidt de Persoon van de andere personen in de familie. | [optional] 
**persoon_achternaam** | **str** | Gedeelte van de volledige naam van de Persoon ontvangen van de vorige generatie. | [optional] 
**persoon_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Persoon te contacteren. | [optional] 
**persoon_inwonerschap** | [**List[Inwonerschap]**](Inwonerschap.md) | Jurisdictie waarbinnen het Inwonerschap van de Persoon is gedefinieerd. | [optional] 
**publieke_organisatie_voorkeursnaam** | [**PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam**](PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam.md) |  | [optional] 
**publieke_organisatie_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Organisatie te contacteren. | [optional] 
**publieke_organisatie_identificator** | [**List[Identificator]**](Identificator.md) | Identificator die de organisatie uniek identificeert. | [optional] 
**publieke_organisatie_type** | [**PubliekeOrganisatiePubliekeOrganisatieType**](PubliekeOrganisatiePubliekeOrganisatieType.md) |  | [optional] 
**geregistreerde_organisatie_voorkeursnaam** | [**GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam**](GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam.md) |  | [optional] 
**geregistreerde_organisatie_registratie** | [**List[Identificator]**](Identificator.md) |  | 
**geregistreerde_organisatie_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Organisatie te contacteren. | [optional] 
**geregistreerde_organisatie_type** | [**PubliekeOrganisatiePubliekeOrganisatieType**](PubliekeOrganisatiePubliekeOrganisatieType.md) |  | [optional] 
**participatie_rol** | [**ParticipatieParticipatieRol**](ParticipatieParticipatieRol.md) |  | [optional] 
**participatie_heeft_participant** | [**ParticipatieParticipatieHeeftParticipant**](ParticipatieParticipatieHeeftParticipant.md) |  | [optional] 
**publieke_dienstverlening_naam** | [**PubliekeDienstverleningPubliekeDienstverleningNaam**](PubliekeDienstverleningPubliekeDienstverleningNaam.md) |  | 
**publieke_dienstverlening_heeft_verantwoordelijke** | [**PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke**](PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke.md) |  | 
**publieke_dienstverlening_heeft_participatie** | [**List[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner]**](PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner.md) | De Agenten die deelnemen aan de Publieke Dienstverlening. | [optional] 
**publieke_dienstverlening_gebruikt** | [**List[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner]**](GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner.md) | Referenties naar alle Inputs die de Publieke Dienstverlening gebruikt om een of meerdere Outputs te produceren. | [optional] 
**publieke_dienstverlening_produceert** | [**List[PubliekeDienstverleningPubliekeDienstverleningProduceertInner]**](PubliekeDienstverleningPubliekeDienstverleningProduceertInner.md) | De referenties naar alle resources die de Publieke Dienstverlening produceert. | [optional] 
**publieke_dienstverlening_type** | [**PubliekeDienstverleningPubliekeDienstverleningType**](PubliekeDienstverleningPubliekeDienstverleningType.md) |  | [optional] 
**publieke_dienstverlening_finaliteit** | [**PubliekeDienstverleningPubliekeDienstverleningFinaliteit**](PubliekeDienstverleningPubliekeDienstverleningFinaliteit.md) |  | [optional] 
**activeringstraject_naam** | [**ActiveringstrajectActiveringstrajectNaam**](ActiveringstrajectActiveringstrajectNaam.md) |  | 
**activeringstraject_startdatum** | [**ActiveringstrajectActiveringstrajectStartdatum**](ActiveringstrajectActiveringstrajectStartdatum.md) |  | [optional] 
**activeringstraject_einddatum** | [**ActiveringstrajectActiveringstrajectEinddatum**](ActiveringstrajectActiveringstrajectEinddatum.md) |  | [optional] 
**activeringstraject_status** | [**ActiveringstrajectActiveringstrajectStatus**](ActiveringstrajectActiveringstrajectStatus.md) |  | [optional] 
**activeringstraject_deeltraject** | [**List[Deeltraject]**](Deeltraject.md) | De Deeltrajecten gelinkt aan dit Traject. | [optional] 
**activeringstraject_heeft_participatie** | [**List[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner]**](PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner.md) |  | [optional] 
**deeltraject_naam** | [**DeeltrajectDeeltrajectNaam**](DeeltrajectDeeltrajectNaam.md) |  | [optional] 
**deeltraject_startdatum** | [**DeeltrajectDeeltrajectStartdatum**](DeeltrajectDeeltrajectStartdatum.md) |  | [optional] 
**deeltraject_einddatum** | [**DeeltrajectDeeltrajectEinddatum**](DeeltrajectDeeltrajectEinddatum.md) |  | [optional] 
**deeltraject_type** | [**DeeltrajectDeeltrajectType**](DeeltrajectDeeltrajectType.md) |  | [optional] 
**deeltraject_status** | [**DeeltrajectDeeltrajectStatus**](DeeltrajectDeeltrajectStatus.md) |  | [optional] 
**deeltraject_heeft_participatie** | [**List[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner]**](PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner.md) |  | [optional] 
**verblijfplaats_verblijfsadres** | [**ContactpuntContactpuntAdres**](ContactpuntContactpuntAdres.md) |  | [optional] 
**adresvoorstelling_straatnaam** | [**AdresvoorstellingAdresvoorstellingStraatnaam**](AdresvoorstellingAdresvoorstellingStraatnaam.md) |  | [optional] 
**adresvoorstelling_straatcode** | [**AdresvoorstellingAdresvoorstellingStraatcode**](AdresvoorstellingAdresvoorstellingStraatcode.md) |  | [optional] 
**adresvoorstelling_busnummer** | [**AdresvoorstellingAdresvoorstellingBusnummer**](AdresvoorstellingAdresvoorstellingBusnummer.md) |  | [optional] 
**adresvoorstelling_huisnummer** | [**AdresvoorstellingAdresvoorstellingHuisnummer**](AdresvoorstellingAdresvoorstellingHuisnummer.md) |  | [optional] 
**adresvoorstelling_postcode** | [**AdresvoorstellingAdresvoorstellingPostcode**](AdresvoorstellingAdresvoorstellingPostcode.md) |  | [optional] 
**adresvoorstelling_gemeentenaam** | [**AdresvoorstellingAdresvoorstellingGemeentenaam**](AdresvoorstellingAdresvoorstellingGemeentenaam.md) |  | [optional] 
**adresvoorstelling_gemeentecode** | [**AdresvoorstellingAdresvoorstellingGemeentecode**](AdresvoorstellingAdresvoorstellingGemeentecode.md) |  | [optional] 
**adresvoorstelling_land** | [**AdresvoorstellingAdresvoorstellingLand**](AdresvoorstellingAdresvoorstellingLand.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_ld_root_graph_inner import JsonLdRootGraphInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLdRootGraphInner from a JSON string
json_ld_root_graph_inner_instance = JsonLdRootGraphInner.from_json(json)
# print the JSON string representation of the object
print(JsonLdRootGraphInner.to_json())

# convert the object into a dict
json_ld_root_graph_inner_dict = json_ld_root_graph_inner_instance.to_dict()
# create an instance of JsonLdRootGraphInner from a dict
json_ld_root_graph_inner_from_dict = JsonLdRootGraphInner.from_dict(json_ld_root_graph_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


