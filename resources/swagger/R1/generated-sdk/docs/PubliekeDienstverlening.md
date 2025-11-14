# PubliekeDienstverlening

Een publieke dienstverlening is een geheel van verplichte of optioneel uitgevoerde of uitvoerbare acties door of in naam van een publieke organisatie. De dienstverlening is ten bate van een individu, een bedrijf, een andere publieke organisatie of groepen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**publieke_dienstverlening_naam** | [**PubliekeDienstverleningPubliekeDienstverleningNaam**](PubliekeDienstverleningPubliekeDienstverleningNaam.md) |  | 
**publieke_dienstverlening_heeft_verantwoordelijke** | [**PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke**](PubliekeDienstverleningPubliekeDienstverleningHeeftVerantwoordelijke.md) |  | 
**publieke_dienstverlening_heeft_participatie** | [**List[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner]**](PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner.md) | De Agenten die deelnemen aan de Publieke Dienstverlening. | [optional] 
**publieke_dienstverlening_gebruikt** | [**List[GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner]**](GeregistreerdPersoonGeregistreerdPersoonWerkvoorkeurenInner.md) | Referenties naar alle Inputs die de Publieke Dienstverlening gebruikt om een of meerdere Outputs te produceren. | [optional] 
**publieke_dienstverlening_produceert** | [**List[PubliekeDienstverleningPubliekeDienstverleningProduceertInner]**](PubliekeDienstverleningPubliekeDienstverleningProduceertInner.md) | De referenties naar alle resources die de Publieke Dienstverlening produceert. | [optional] 
**publieke_dienstverlening_type** | [**PubliekeDienstverleningPubliekeDienstverleningType**](PubliekeDienstverleningPubliekeDienstverleningType.md) |  | [optional] 
**publieke_dienstverlening_finaliteit** | [**PubliekeDienstverleningPubliekeDienstverleningFinaliteit**](PubliekeDienstverleningPubliekeDienstverleningFinaliteit.md) |  | [optional] 

## Example

```python
from openapi_client.models.publieke_dienstverlening import PubliekeDienstverlening

# TODO update the JSON string below
json = "{}"
# create an instance of PubliekeDienstverlening from a JSON string
publieke_dienstverlening_instance = PubliekeDienstverlening.from_json(json)
# print the JSON string representation of the object
print(PubliekeDienstverlening.to_json())

# convert the object into a dict
publieke_dienstverlening_dict = publieke_dienstverlening_instance.to_dict()
# create an instance of PubliekeDienstverlening from a dict
publieke_dienstverlening_from_dict = PubliekeDienstverlening.from_dict(publieke_dienstverlening_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


