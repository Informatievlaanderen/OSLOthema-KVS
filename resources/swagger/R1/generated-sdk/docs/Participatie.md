# Participatie

De rol waarin een Agent deelneemt aan de Publieke Dienstverlening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**participatie_rol** | [**ParticipatieParticipatieRol**](ParticipatieParticipatieRol.md) |  | [optional] 
**participatie_heeft_participant** | [**ParticipatieParticipatieHeeftParticipant**](ParticipatieParticipatieHeeftParticipant.md) |  | [optional] 

## Example

```python
from openapi_client.models.participatie import Participatie

# TODO update the JSON string below
json = "{}"
# create an instance of Participatie from a JSON string
participatie_instance = Participatie.from_json(json)
# print the JSON string representation of the object
print(Participatie.to_json())

# convert the object into a dict
participatie_dict = participatie_instance.to_dict()
# create an instance of Participatie from a dict
participatie_from_dict = Participatie.from_dict(participatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


