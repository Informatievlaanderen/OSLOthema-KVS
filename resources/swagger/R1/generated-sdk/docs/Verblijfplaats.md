# Verblijfplaats

Plaats waar een Persoon al dan niet tijdelijk woont of logeert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | [optional] 
**verblijfplaats_verblijfsadres** | [**ContactpuntContactpuntAdres**](ContactpuntContactpuntAdres.md) |  | [optional] 

## Example

```python
from openapi_client.models.verblijfplaats import Verblijfplaats

# TODO update the JSON string below
json = "{}"
# create an instance of Verblijfplaats from a JSON string
verblijfplaats_instance = Verblijfplaats.from_json(json)
# print the JSON string representation of the object
print(Verblijfplaats.to_json())

# convert the object into a dict
verblijfplaats_dict = verblijfplaats_instance.to_dict()
# create an instance of Verblijfplaats from a dict
verblijfplaats_from_dict = Verblijfplaats.from_dict(verblijfplaats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


