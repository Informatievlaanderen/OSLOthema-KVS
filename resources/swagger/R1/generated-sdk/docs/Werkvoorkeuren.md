# Werkvoorkeuren

De voorkeuren van de Werkzoekende bij het zoeken naar werk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | 
**type** | **str** | Object type. | 
**werkvoorkeuren_beroep** | [**List[Beroepstoestand]**](Beroepstoestand.md) | Voorkeuren voor bepaalde beroepen. | [optional] 

## Example

```python
from openapi_client.models.werkvoorkeuren import Werkvoorkeuren

# TODO update the JSON string below
json = "{}"
# create an instance of Werkvoorkeuren from a JSON string
werkvoorkeuren_instance = Werkvoorkeuren.from_json(json)
# print the JSON string representation of the object
print(Werkvoorkeuren.to_json())

# convert the object into a dict
werkvoorkeuren_dict = werkvoorkeuren_instance.to_dict()
# create an instance of Werkvoorkeuren from a dict
werkvoorkeuren_from_dict = Werkvoorkeuren.from_dict(werkvoorkeuren_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


