# JsonLdRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**List[JsonLdRootContextInner]**](JsonLdRootContextInner.md) | JSON-LD&#39;s context which defines how the JSON-LD keys are mapped to URIs. | [optional] 
**graph** | [**List[JsonLdRootGraphInner]**](JsonLdRootGraphInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_ld_root import JsonLdRoot

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLdRoot from a JSON string
json_ld_root_instance = JsonLdRoot.from_json(json)
# print the JSON string representation of the object
print(JsonLdRoot.to_json())

# convert the object into a dict
json_ld_root_dict = json_ld_root_instance.to_dict()
# create an instance of JsonLdRoot from a dict
json_ld_root_from_dict = JsonLdRoot.from_dict(json_ld_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


