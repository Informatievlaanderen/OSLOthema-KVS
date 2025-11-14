# PubliekeDienstverleningPubliekeDienstverleningFinaliteit

Wettelijk kader waarvoor de informatie wordt bevraagd.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to a FinaliteitType enum value URI. | 
**skos_pref_label** | [**PubliekeDienstverleningPubliekeDienstverleningFinaliteitSKOSPrefLabel**](PubliekeDienstverleningPubliekeDienstverleningFinaliteitSKOSPrefLabel.md) |  | 

## Example

```python
from openapi_client.models.publieke_dienstverlening_publieke_dienstverlening_finaliteit import PubliekeDienstverleningPubliekeDienstverleningFinaliteit

# TODO update the JSON string below
json = "{}"
# create an instance of PubliekeDienstverleningPubliekeDienstverleningFinaliteit from a JSON string
publieke_dienstverlening_publieke_dienstverlening_finaliteit_instance = PubliekeDienstverleningPubliekeDienstverleningFinaliteit.from_json(json)
# print the JSON string representation of the object
print(PubliekeDienstverleningPubliekeDienstverleningFinaliteit.to_json())

# convert the object into a dict
publieke_dienstverlening_publieke_dienstverlening_finaliteit_dict = publieke_dienstverlening_publieke_dienstverlening_finaliteit_instance.to_dict()
# create an instance of PubliekeDienstverleningPubliekeDienstverleningFinaliteit from a dict
publieke_dienstverlening_publieke_dienstverlening_finaliteit_from_dict = PubliekeDienstverleningPubliekeDienstverleningFinaliteit.from_dict(publieke_dienstverlening_publieke_dienstverlening_finaliteit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


