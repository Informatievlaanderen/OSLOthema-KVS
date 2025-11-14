# Beroepstoestand

Voorkeur voor een bepaald beroep.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type. | 
**beroepstoestand_naam** | [**BeroepstoestandBeroepstoestandNaam**](BeroepstoestandBeroepstoestandNaam.md) |  | [optional] 
**beroepstoestand_voorkeur** | [**BeroepstoestandBeroepstoestandVoorkeur**](BeroepstoestandBeroepstoestandVoorkeur.md) |  | [optional] 

## Example

```python
from openapi_client.models.beroepstoestand import Beroepstoestand

# TODO update the JSON string below
json = "{}"
# create an instance of Beroepstoestand from a JSON string
beroepstoestand_instance = Beroepstoestand.from_json(json)
# print the JSON string representation of the object
print(Beroepstoestand.to_json())

# convert the object into a dict
beroepstoestand_dict = beroepstoestand_instance.to_dict()
# create an instance of Beroepstoestand from a dict
beroepstoestand_from_dict = Beroepstoestand.from_dict(beroepstoestand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


