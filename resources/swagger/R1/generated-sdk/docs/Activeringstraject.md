# Activeringstraject

Een Activeringstraject is een specifiekere variant van een Traject dat moet aansporen om de Werkzoekende te activeren naar werk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**activeringstraject_naam** | [**ActiveringstrajectActiveringstrajectNaam**](ActiveringstrajectActiveringstrajectNaam.md) |  | 
**activeringstraject_startdatum** | [**ActiveringstrajectActiveringstrajectStartdatum**](ActiveringstrajectActiveringstrajectStartdatum.md) |  | [optional] 
**activeringstraject_einddatum** | [**ActiveringstrajectActiveringstrajectEinddatum**](ActiveringstrajectActiveringstrajectEinddatum.md) |  | [optional] 
**activeringstraject_status** | [**ActiveringstrajectActiveringstrajectStatus**](ActiveringstrajectActiveringstrajectStatus.md) |  | [optional] 
**activeringstraject_deeltraject** | [**List[Deeltraject]**](Deeltraject.md) | De Deeltrajecten gelinkt aan dit Traject. | [optional] 
**activeringstraject_heeft_participatie** | [**List[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner]**](PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.activeringstraject import Activeringstraject

# TODO update the JSON string below
json = "{}"
# create an instance of Activeringstraject from a JSON string
activeringstraject_instance = Activeringstraject.from_json(json)
# print the JSON string representation of the object
print(Activeringstraject.to_json())

# convert the object into a dict
activeringstraject_dict = activeringstraject_instance.to_dict()
# create an instance of Activeringstraject from a dict
activeringstraject_from_dict = Activeringstraject.from_dict(activeringstraject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


