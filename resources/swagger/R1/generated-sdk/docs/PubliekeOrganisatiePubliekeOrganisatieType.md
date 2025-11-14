# PubliekeOrganisatiePubliekeOrganisatieType

Het soort Organisatie.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to a OrganisatieType enum value URI. | 
**skos_pref_label** | [**PubliekeOrganisatiePubliekeOrganisatieTypeSKOSPrefLabel**](PubliekeOrganisatiePubliekeOrganisatieTypeSKOSPrefLabel.md) |  | 

## Example

```python
from openapi_client.models.publieke_organisatie_publieke_organisatie_type import PubliekeOrganisatiePubliekeOrganisatieType

# TODO update the JSON string below
json = "{}"
# create an instance of PubliekeOrganisatiePubliekeOrganisatieType from a JSON string
publieke_organisatie_publieke_organisatie_type_instance = PubliekeOrganisatiePubliekeOrganisatieType.from_json(json)
# print the JSON string representation of the object
print(PubliekeOrganisatiePubliekeOrganisatieType.to_json())

# convert the object into a dict
publieke_organisatie_publieke_organisatie_type_dict = publieke_organisatie_publieke_organisatie_type_instance.to_dict()
# create an instance of PubliekeOrganisatiePubliekeOrganisatieType from a dict
publieke_organisatie_publieke_organisatie_type_from_dict = PubliekeOrganisatiePubliekeOrganisatieType.from_dict(publieke_organisatie_publieke_organisatie_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


