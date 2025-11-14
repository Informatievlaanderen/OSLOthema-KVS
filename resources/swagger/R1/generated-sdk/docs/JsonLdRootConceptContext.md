# JsonLdRootConceptContext

JSON-LD's context which defines how the JSON-LD keys are mapped to URIs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skos** | **str** | W3C SKOS vocabulary URI. | [optional] 

## Example

```python
from openapi_client.models.json_ld_root_concept_context import JsonLdRootConceptContext

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLdRootConceptContext from a JSON string
json_ld_root_concept_context_instance = JsonLdRootConceptContext.from_json(json)
# print the JSON string representation of the object
print(JsonLdRootConceptContext.to_json())

# convert the object into a dict
json_ld_root_concept_context_dict = json_ld_root_concept_context_instance.to_dict()
# create an instance of JsonLdRootConceptContext from a dict
json_ld_root_concept_context_from_dict = JsonLdRootConceptContext.from_dict(json_ld_root_concept_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


