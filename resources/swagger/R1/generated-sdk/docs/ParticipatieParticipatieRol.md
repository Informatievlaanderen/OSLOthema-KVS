# ParticipatieParticipatieRol

De functie van de Agent bij het deelnemen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to a Participatietype enum value URI. | 
**skos_pref_label** | [**ParticipatieParticipatieRolSKOSPrefLabel**](ParticipatieParticipatieRolSKOSPrefLabel.md) |  | 

## Example

```python
from openapi_client.models.participatie_participatie_rol import ParticipatieParticipatieRol

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipatieParticipatieRol from a JSON string
participatie_participatie_rol_instance = ParticipatieParticipatieRol.from_json(json)
# print the JSON string representation of the object
print(ParticipatieParticipatieRol.to_json())

# convert the object into a dict
participatie_participatie_rol_dict = participatie_participatie_rol_instance.to_dict()
# create an instance of ParticipatieParticipatieRol from a dict
participatie_participatie_rol_from_dict = ParticipatieParticipatieRol.from_dict(participatie_participatie_rol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


