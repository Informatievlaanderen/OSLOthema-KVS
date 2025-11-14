# GeregistreerdeOrganisatie

Organisatie met een juridisch statuut vastgelegd door registratie. Vergelijk met een FormeleOrganisatie waarbij dit statuut ook op een andere manier verkregen kan zijn.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**geregistreerde_organisatie_voorkeursnaam** | [**GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam**](GeregistreerdeOrganisatieGeregistreerdeOrganisatieVoorkeursnaam.md) |  | [optional] 
**geregistreerde_organisatie_registratie** | [**List[Identificator]**](Identificator.md) |  | 
**geregistreerde_organisatie_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Organisatie te contacteren. | [optional] 
**geregistreerde_organisatie_type** | [**PubliekeOrganisatiePubliekeOrganisatieType**](PubliekeOrganisatiePubliekeOrganisatieType.md) |  | [optional] 

## Example

```python
from openapi_client.models.geregistreerde_organisatie import GeregistreerdeOrganisatie

# TODO update the JSON string below
json = "{}"
# create an instance of GeregistreerdeOrganisatie from a JSON string
geregistreerde_organisatie_instance = GeregistreerdeOrganisatie.from_json(json)
# print the JSON string representation of the object
print(GeregistreerdeOrganisatie.to_json())

# convert the object into a dict
geregistreerde_organisatie_dict = geregistreerde_organisatie_instance.to_dict()
# create an instance of GeregistreerdeOrganisatie from a dict
geregistreerde_organisatie_from_dict = GeregistreerdeOrganisatie.from_dict(geregistreerde_organisatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


