# openapi_client.DienstverleningApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service**](DienstverleningApi.md#get_service) | **GET** /v1/dienstverleningen | Dienstverlening informatie opvragen.


# **get_service**
> JsonLdRoot get_service(x_correlation_id, x_insz)

Dienstverlening informatie opvragen.

Vraag alle informatie op over een Dienstverlening tussen Organisaties en Personen zoals een Activeringstraject van een Werkzoekende door de Organisatie VDAB. Iedere Dienstverlening tussen Organisatie - Personen heeft zijn eigen ID.

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
    api_instance = openapi_client.DienstverleningApi(api_client)
    x_correlation_id = 'x_correlation_id_example' # str | Random UUID om het request te identificeren.
    x_insz = '42061467820' # str | INSZ code van de Werkzoekende.

    try:
        # Dienstverlening informatie opvragen.
        api_response = api_instance.get_service(x_correlation_id, x_insz)
        print("The response of DienstverleningApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DienstverleningApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_correlation_id** | **str**| Random UUID om het request te identificeren. | 
 **x_insz** | **str**| INSZ code van de Werkzoekende. | 

### Return type

[**JsonLdRoot**](JsonLdRoot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opvraging succesvol. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

