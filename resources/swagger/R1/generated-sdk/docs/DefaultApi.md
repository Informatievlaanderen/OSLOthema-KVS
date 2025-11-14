# openapi_client.DefaultApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_skos_concept**](DefaultApi.md#get_skos_concept) | **GET** /id/concept/{Concept} | 


# **get_skos_concept**
> JsonLdRoot get_skos_concept(concept)

### Example


```python
import openapi_client
from openapi_client.models.json_ld_root import JsonLdRoot
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    concept = 'VoorkeurType' # str | Concept dat opgevraagd moet worden.

    try:
        api_response = api_instance.get_skos_concept(concept)
        print("The response of DefaultApi->get_skos_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_skos_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept** | **str**| Concept dat opgevraagd moet worden. | 

### Return type

[**JsonLdRoot**](JsonLdRoot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opvraging successvol. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

