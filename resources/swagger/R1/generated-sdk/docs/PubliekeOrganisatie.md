# PubliekeOrganisatie

Een Organisatie die volgens een wettelijk kader behoort tot de publieke sector, ongeacht het bestuursniveau waarop dat kader van kracht is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**publieke_organisatie_voorkeursnaam** | [**PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam**](PubliekeOrganisatiePubliekeOrganisatieVoorkeursnaam.md) |  | [optional] 
**publieke_organisatie_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Organisatie te contacteren. | [optional] 
**publieke_organisatie_identificator** | [**List[Identificator]**](Identificator.md) | Identificator die de organisatie uniek identificeert. | [optional] 
**publieke_organisatie_type** | [**PubliekeOrganisatiePubliekeOrganisatieType**](PubliekeOrganisatiePubliekeOrganisatieType.md) |  | [optional] 

## Example

```python
from openapi_client.models.publieke_organisatie import PubliekeOrganisatie

# TODO update the JSON string below
json = "{}"
# create an instance of PubliekeOrganisatie from a JSON string
publieke_organisatie_instance = PubliekeOrganisatie.from_json(json)
# print the JSON string representation of the object
print(PubliekeOrganisatie.to_json())

# convert the object into a dict
publieke_organisatie_dict = publieke_organisatie_instance.to_dict()
# create an instance of PubliekeOrganisatie from a dict
publieke_organisatie_from_dict = PubliekeOrganisatie.from_dict(publieke_organisatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


