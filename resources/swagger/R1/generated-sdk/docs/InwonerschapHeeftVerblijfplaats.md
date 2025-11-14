# InwonerschapHeeftVerblijfplaats

Plaats waar een persoon verblijft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | [optional] 
**verblijfplaats_verblijfsadres** | [**ContactpuntContactpuntAdres**](ContactpuntContactpuntAdres.md) |  | [optional] 

## Example

```python
from openapi_client.models.inwonerschap_heeft_verblijfplaats import InwonerschapHeeftVerblijfplaats

# TODO update the JSON string below
json = "{}"
# create an instance of InwonerschapHeeftVerblijfplaats from a JSON string
inwonerschap_heeft_verblijfplaats_instance = InwonerschapHeeftVerblijfplaats.from_json(json)
# print the JSON string representation of the object
print(InwonerschapHeeftVerblijfplaats.to_json())

# convert the object into a dict
inwonerschap_heeft_verblijfplaats_dict = inwonerschap_heeft_verblijfplaats_instance.to_dict()
# create an instance of InwonerschapHeeftVerblijfplaats from a dict
inwonerschap_heeft_verblijfplaats_from_dict = InwonerschapHeeftVerblijfplaats.from_dict(inwonerschap_heeft_verblijfplaats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


