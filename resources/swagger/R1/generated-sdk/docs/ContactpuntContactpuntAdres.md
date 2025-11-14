# ContactpuntContactpuntAdres

Adres dat men kan aanschrijven of bezoeken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to an Adresvoorstelling instance. | 

## Example

```python
from openapi_client.models.contactpunt_contactpunt_adres import ContactpuntContactpuntAdres

# TODO update the JSON string below
json = "{}"
# create an instance of ContactpuntContactpuntAdres from a JSON string
contactpunt_contactpunt_adres_instance = ContactpuntContactpuntAdres.from_json(json)
# print the JSON string representation of the object
print(ContactpuntContactpuntAdres.to_json())

# convert the object into a dict
contactpunt_contactpunt_adres_dict = contactpunt_contactpunt_adres_instance.to_dict()
# create an instance of ContactpuntContactpuntAdres from a dict
contactpunt_contactpunt_adres_from_dict = ContactpuntContactpuntAdres.from_dict(contactpunt_contactpunt_adres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


