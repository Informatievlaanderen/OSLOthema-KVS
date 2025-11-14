import openapi_client
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
    x_correlation_id = '073080ce-cf0c-4c2f-b709-8570115c91ec' # str | Random UUID om het request te identificeren.
    x_insz = '42061467820' # str | INSZ code van de Werkzoekende.

    try:
        # Dienstverlening informatie opvragen.
        api_response = api_instance.get_service(x_correlation_id, x_insz)
        print("The response of DienstverleningApi->get_service:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DienstverleningApi->get_service: %s\n" % e)
