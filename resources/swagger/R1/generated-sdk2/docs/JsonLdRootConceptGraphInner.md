# JsonLdRootConceptGraphInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | URI dat het Concept uniek refereert. | 
**type** | **str** | Object type. | 
**skos_pref_label** | [**DeeltrajectConceptSKOSPrefLabel**](DeeltrajectConceptSKOSPrefLabel.md) |  | 
**skos_definition** | [**DeeltrajectConceptSKOSDefinition**](DeeltrajectConceptSKOSDefinition.md) |  | 
**skos_inscheme** | [**DeeltrajectConceptSKOSInscheme**](DeeltrajectConceptSKOSInscheme.md) |  | [optional] 
**skos_top_concept_of** | [**DeeltrajectConceptSKOSTopConceptOf**](DeeltrajectConceptSKOSTopConceptOf.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_ld_root_concept_graph_inner import JsonLdRootConceptGraphInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLdRootConceptGraphInner from a JSON string
json_ld_root_concept_graph_inner_instance = JsonLdRootConceptGraphInner.from_json(json)
# print the JSON string representation of the object
print(JsonLdRootConceptGraphInner.to_json())

# convert the object into a dict
json_ld_root_concept_graph_inner_dict = json_ld_root_concept_graph_inner_instance.to_dict()
# create an instance of JsonLdRootConceptGraphInner from a dict
json_ld_root_concept_graph_inner_from_dict = JsonLdRootConceptGraphInner.from_dict(json_ld_root_concept_graph_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


