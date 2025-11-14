# Deeltraject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**deeltraject_naam** | [**DeeltrajectDeeltrajectNaam**](DeeltrajectDeeltrajectNaam.md) |  | [optional] 
**deeltraject_startdatum** | [**DeeltrajectDeeltrajectStartdatum**](DeeltrajectDeeltrajectStartdatum.md) |  | [optional] 
**deeltraject_einddatum** | [**DeeltrajectDeeltrajectEinddatum**](DeeltrajectDeeltrajectEinddatum.md) |  | [optional] 
**deeltraject_type** | [**DeeltrajectDeeltrajectType**](DeeltrajectDeeltrajectType.md) |  | [optional] 
**deeltraject_status** | [**DeeltrajectDeeltrajectStatus**](DeeltrajectDeeltrajectStatus.md) |  | [optional] 
**deeltraject_heeft_participatie** | [**List[PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner]**](PubliekeDienstverleningPubliekeDienstverleningHeeftParticipatieInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.deeltraject import Deeltraject

# TODO update the JSON string below
json = "{}"
# create an instance of Deeltraject from a JSON string
deeltraject_instance = Deeltraject.from_json(json)
# print the JSON string representation of the object
print(Deeltraject.to_json())

# convert the object into a dict
deeltraject_dict = deeltraject_instance.to_dict()
# create an instance of Deeltraject from a dict
deeltraject_from_dict = Deeltraject.from_dict(deeltraject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


