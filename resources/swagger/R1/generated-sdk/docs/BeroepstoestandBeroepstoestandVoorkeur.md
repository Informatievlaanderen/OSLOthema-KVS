# BeroepstoestandBeroepstoestandVoorkeur

De soort voorkeur voor een bepaald beroep.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. Must point to a Voorkeurtype enum value URI. | 
**skos_pref_label** | [**BeroepstoestandBeroepstoestandVoorkeurSKOSPrefLabel**](BeroepstoestandBeroepstoestandVoorkeurSKOSPrefLabel.md) |  | 

## Example

```python
from openapi_client.models.beroepstoestand_beroepstoestand_voorkeur import BeroepstoestandBeroepstoestandVoorkeur

# TODO update the JSON string below
json = "{}"
# create an instance of BeroepstoestandBeroepstoestandVoorkeur from a JSON string
beroepstoestand_beroepstoestand_voorkeur_instance = BeroepstoestandBeroepstoestandVoorkeur.from_json(json)
# print the JSON string representation of the object
print(BeroepstoestandBeroepstoestandVoorkeur.to_json())

# convert the object into a dict
beroepstoestand_beroepstoestand_voorkeur_dict = beroepstoestand_beroepstoestand_voorkeur_instance.to_dict()
# create an instance of BeroepstoestandBeroepstoestandVoorkeur from a dict
beroepstoestand_beroepstoestand_voorkeur_from_dict = BeroepstoestandBeroepstoestandVoorkeur.from_dict(beroepstoestand_beroepstoestand_voorkeur_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


