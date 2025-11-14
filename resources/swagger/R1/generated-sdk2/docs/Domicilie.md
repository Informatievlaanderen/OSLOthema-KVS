# Domicilie

Plaats waar een Persoon al dan niet tijdelijk woont of logeert. Specifieker type van Verblijfplaats, erft alle attributen over.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | [optional] 
**verblijfplaats_verblijfsadres** | [**ContactpuntContactpuntAdres**](ContactpuntContactpuntAdres.md) |  | [optional] 

## Example

```python
from openapi_client.models.domicilie import Domicilie

# TODO update the JSON string below
json = "{}"
# create an instance of Domicilie from a JSON string
domicilie_instance = Domicilie.from_json(json)
# print the JSON string representation of the object
print(Domicilie.to_json())

# convert the object into a dict
domicilie_dict = domicilie_instance.to_dict()
# create an instance of Domicilie from a dict
domicilie_from_dict = Domicilie.from_dict(domicilie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


