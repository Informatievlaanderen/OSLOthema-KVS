# Inwonerschap

Het feit dat een persoon verblijf houdt in een plaats of land.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | [optional] 
**heeft_verblijfplaats** | [**InwonerschapHeeftVerblijfplaats**](InwonerschapHeeftVerblijfplaats.md) |  | [optional] 

## Example

```python
from openapi_client.models.inwonerschap import Inwonerschap

# TODO update the JSON string below
json = "{}"
# create an instance of Inwonerschap from a JSON string
inwonerschap_instance = Inwonerschap.from_json(json)
# print the JSON string representation of the object
print(Inwonerschap.to_json())

# convert the object into a dict
inwonerschap_dict = inwonerschap_instance.to_dict()
# create an instance of Inwonerschap from a dict
inwonerschap_from_dict = Inwonerschap.from_dict(inwonerschap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


