# Adresvoorstelling

Meer leesbare voorstelling met enkel de basisgegevens van het adres, bedoeld voor het gebruik van een adres als attribuut van een ander object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID. Can be an URI or internal reference such as _:MyID. | [optional] 
**type** | **str** | Object type. | 
**adresvoorstelling_straatnaam** | [**AdresvoorstellingAdresvoorstellingStraatnaam**](AdresvoorstellingAdresvoorstellingStraatnaam.md) |  | [optional] 
**adresvoorstelling_straatcode** | [**AdresvoorstellingAdresvoorstellingStraatcode**](AdresvoorstellingAdresvoorstellingStraatcode.md) |  | [optional] 
**adresvoorstelling_busnummer** | [**AdresvoorstellingAdresvoorstellingBusnummer**](AdresvoorstellingAdresvoorstellingBusnummer.md) |  | [optional] 
**adresvoorstelling_huisnummer** | [**AdresvoorstellingAdresvoorstellingHuisnummer**](AdresvoorstellingAdresvoorstellingHuisnummer.md) |  | [optional] 
**adresvoorstelling_postcode** | [**AdresvoorstellingAdresvoorstellingPostcode**](AdresvoorstellingAdresvoorstellingPostcode.md) |  | [optional] 
**adresvoorstelling_gemeentenaam** | [**AdresvoorstellingAdresvoorstellingGemeentenaam**](AdresvoorstellingAdresvoorstellingGemeentenaam.md) |  | [optional] 
**adresvoorstelling_gemeentecode** | [**AdresvoorstellingAdresvoorstellingGemeentecode**](AdresvoorstellingAdresvoorstellingGemeentecode.md) |  | [optional] 
**adresvoorstelling_land** | [**AdresvoorstellingAdresvoorstellingLand**](AdresvoorstellingAdresvoorstellingLand.md) |  | [optional] 

## Example

```python
from openapi_client.models.adresvoorstelling import Adresvoorstelling

# TODO update the JSON string below
json = "{}"
# create an instance of Adresvoorstelling from a JSON string
adresvoorstelling_instance = Adresvoorstelling.from_json(json)
# print the JSON string representation of the object
print(Adresvoorstelling.to_json())

# convert the object into a dict
adresvoorstelling_dict = adresvoorstelling_instance.to_dict()
# create an instance of Adresvoorstelling from a dict
adresvoorstelling_from_dict = Adresvoorstelling.from_dict(adresvoorstelling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


