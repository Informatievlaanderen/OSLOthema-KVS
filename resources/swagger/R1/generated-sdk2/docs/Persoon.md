# Persoon

Natuurlijk persoon.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**persoon_voornaam** | **str** | Naam die een Persoon bij geboorte wordt gegeven. Onderscheidt de Persoon van de andere personen in de familie. | [optional] 
**persoon_achternaam** | **str** | Gedeelte van de volledige naam van de Persoon ontvangen van de vorige generatie. | [optional] 
**persoon_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Persoon te contacteren. | [optional] 
**persoon_inwonerschap** | [**List[Inwonerschap]**](Inwonerschap.md) | Jurisdictie waarbinnen het Inwonerschap van de Persoon is gedefinieerd. | [optional] 

## Example

```python
from openapi_client.models.persoon import Persoon

# TODO update the JSON string below
json = "{}"
# create an instance of Persoon from a JSON string
persoon_instance = Persoon.from_json(json)
# print the JSON string representation of the object
print(Persoon.to_json())

# convert the object into a dict
persoon_dict = persoon_instance.to_dict()
# create an instance of Persoon from a dict
persoon_from_dict = Persoon.from_dict(persoon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


