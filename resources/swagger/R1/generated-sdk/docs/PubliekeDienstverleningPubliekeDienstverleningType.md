# PubliekeDienstverleningPubliekeDienstverleningType

Het soort Publieke Dienstverlening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to a PubliekeDienstverleningType enum value URI. | 
**skos_pref_label** | [**PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel**](PubliekeDienstverleningPubliekeDienstverleningTypeSKOSPrefLabel.md) |  | 

## Example

```python
from openapi_client.models.publieke_dienstverlening_publieke_dienstverlening_type import PubliekeDienstverleningPubliekeDienstverleningType

# TODO update the JSON string below
json = "{}"
# create an instance of PubliekeDienstverleningPubliekeDienstverleningType from a JSON string
publieke_dienstverlening_publieke_dienstverlening_type_instance = PubliekeDienstverleningPubliekeDienstverleningType.from_json(json)
# print the JSON string representation of the object
print(PubliekeDienstverleningPubliekeDienstverleningType.to_json())

# convert the object into a dict
publieke_dienstverlening_publieke_dienstverlening_type_dict = publieke_dienstverlening_publieke_dienstverlening_type_instance.to_dict()
# create an instance of PubliekeDienstverleningPubliekeDienstverleningType from a dict
publieke_dienstverlening_publieke_dienstverlening_type_from_dict = PubliekeDienstverleningPubliekeDienstverleningType.from_dict(publieke_dienstverlening_publieke_dienstverlening_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


