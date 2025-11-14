# GeregistreerdPersoon

Persoon waarvan de gegevens zijn ingeschreven in een register.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**geregistreerd_persoon_registratie** | [**List[Identificator]**](Identificator.md) | Identificatiecode van de persoon in het register. | 
**geregistreerd_persoon_voornaam** | **str** | Naam die een Persoon bij geboorte wordt gegeven. Onderscheidt de Persoon van de andere personen in de familie. | [optional] 
**geregistreerd_persoon_achternaam** | **str** | Gedeelte van de volledige naam van de Persoon ontvangen van de vorige generatie. | [optional] 
**geregistreerd_persoon_werkvoorkeuren** | [**List[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner]**](GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner.md) | De voorkeuren voor werk van een Persoon. | [optional] 
**geregistreerd_persoon_contactinfo** | [**List[Contactpunt]**](Contactpunt.md) | Informatie zoals email, telefoon... die toelaat de Persoon te contacteren. | [optional] 
**geregistreerd_persoon_inwonerschap** | [**List[Inwonerschap]**](Inwonerschap.md) | Jurisdictie waarbinnen het Inwonerschap van de Persoon is gedefinieerd. | [optional] 

## Example

```python
from openapi_client.models.geregistreerd_persoon import GeregistreerdPersoon

# TODO update the JSON string below
json = "{}"
# create an instance of GeregistreerdPersoon from a JSON string
geregistreerd_persoon_instance = GeregistreerdPersoon.from_json(json)
# print the JSON string representation of the object
print(GeregistreerdPersoon.to_json())

# convert the object into a dict
geregistreerd_persoon_dict = geregistreerd_persoon_instance.to_dict()
# create an instance of GeregistreerdPersoon from a dict
geregistreerd_persoon_from_dict = GeregistreerdPersoon.from_dict(geregistreerd_persoon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


