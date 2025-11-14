# DeeltrajectDeeltrajectStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to a TrajectStatus enum value URI. | 
**skos_pref_label** | [**DeeltrajectDeeltrajectStatusSKOSPrefLabel**](DeeltrajectDeeltrajectStatusSKOSPrefLabel.md) |  | 

## Example

```python
from openapi_client.models.deeltraject_deeltraject_status import DeeltrajectDeeltrajectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeeltrajectDeeltrajectStatus from a JSON string
deeltraject_deeltraject_status_instance = DeeltrajectDeeltrajectStatus.from_json(json)
# print the JSON string representation of the object
print(DeeltrajectDeeltrajectStatus.to_json())

# convert the object into a dict
deeltraject_deeltraject_status_dict = deeltraject_deeltraject_status_instance.to_dict()
# create an instance of DeeltrajectDeeltrajectStatus from a dict
deeltraject_deeltraject_status_from_dict = DeeltrajectDeeltrajectStatus.from_dict(deeltraject_deeltraject_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


