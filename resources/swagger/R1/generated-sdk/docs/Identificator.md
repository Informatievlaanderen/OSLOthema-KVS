# Identificator

Informatie gebruikt om een object uniek te identificeren.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | 
**identificator_identificator** | **str** | String gebruikt om het object uniek te identificeren. | [optional] 
**identificator_toegekend_door_string** | **str** | Naam vd agent die de identificator heeft toegekend. | [optional] 

## Example

```python
from openapi_client.models.identificator import Identificator

# TODO update the JSON string below
json = "{}"
# create an instance of Identificator from a JSON string
identificator_instance = Identificator.from_json(json)
# print the JSON string representation of the object
print(Identificator.to_json())

# convert the object into a dict
identificator_dict = identificator_instance.to_dict()
# create an instance of Identificator from a dict
identificator_from_dict = Identificator.from_dict(identificator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


