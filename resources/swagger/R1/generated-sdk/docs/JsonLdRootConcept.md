# JsonLdRootConcept


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdRootConceptContext**](JsonLdRootConceptContext.md) |  | [optional] 
**graph** | [**List[JsonLdRootConceptGraphInner]**](JsonLdRootConceptGraphInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_ld_root_concept import JsonLdRootConcept

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLdRootConcept from a JSON string
json_ld_root_concept_instance = JsonLdRootConcept.from_json(json)
# print the JSON string representation of the object
print(JsonLdRootConcept.to_json())

# convert the object into a dict
json_ld_root_concept_dict = json_ld_root_concept_instance.to_dict()
# create an instance of JsonLdRootConcept from a dict
json_ld_root_concept_from_dict = JsonLdRootConcept.from_dict(json_ld_root_concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


