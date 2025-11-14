# DeeltrajectConcept

Deeltraject soort

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
from openapi_client.models.deeltraject_concept import DeeltrajectConcept

# TODO update the JSON string below
json = "{}"
# create an instance of DeeltrajectConcept from a JSON string
deeltraject_concept_instance = DeeltrajectConcept.from_json(json)
# print the JSON string representation of the object
print(DeeltrajectConcept.to_json())

# convert the object into a dict
deeltraject_concept_dict = deeltraject_concept_instance.to_dict()
# create an instance of DeeltrajectConcept from a dict
deeltraject_concept_from_dict = DeeltrajectConcept.from_dict(deeltraject_concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


