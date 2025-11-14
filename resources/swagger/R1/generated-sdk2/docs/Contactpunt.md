# Contactpunt

Informatie zoals email, telefoon, adres die toelaat om iemand of iets te contacteren.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | 
**contactpunt_telefoon** | [**ContactpuntContactpuntTelefoon**](ContactpuntContactpuntTelefoon.md) |  | [optional] 
**contactpunt_adres** | [**ContactpuntContactpuntAdres**](ContactpuntContactpuntAdres.md) |  | [optional] 
**contactpunt_email** | [**ContactpuntContactpuntEmail**](ContactpuntContactpuntEmail.md) |  | [optional] 

## Example

```python
from openapi_client.models.contactpunt import Contactpunt

# TODO update the JSON string below
json = "{}"
# create an instance of Contactpunt from a JSON string
contactpunt_instance = Contactpunt.from_json(json)
# print the JSON string representation of the object
print(Contactpunt.to_json())

# convert the object into a dict
contactpunt_dict = contactpunt_instance.to_dict()
# create an instance of Contactpunt from a dict
contactpunt_from_dict = Contactpunt.from_dict(contactpunt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


