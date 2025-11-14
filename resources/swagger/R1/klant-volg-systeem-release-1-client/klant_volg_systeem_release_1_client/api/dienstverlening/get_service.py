from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.json_ld_root import JsonLdRoot
from ...types import Response


def _get_kwargs(
    *,
    x_correlation_id: UUID,
    x_insz: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Correlation-Id"] = x_correlation_id

    headers["X-INSZ"] = x_insz

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dienstverleningen",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | JsonLdRoot | None:
    if response.status_code == 200:
        response_200 = JsonLdRoot.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorMessage.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = ErrorMessage.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorMessage.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorMessage | JsonLdRoot]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_correlation_id: UUID,
    x_insz: str,
) -> Response[ErrorMessage | JsonLdRoot]:
    """Dienstverlening informatie opvragen.

     Vraag alle informatie op over een Dienstverlening tussen Organisaties en Personen zoals een
    Activeringstraject van een Werkzoekende door de Organisatie VDAB. Iedere Dienstverlening tussen
    Organisatie - Personen heeft zijn eigen ID.

    Args:
        x_correlation_id (UUID):
        x_insz (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | JsonLdRoot]
    """

    kwargs = _get_kwargs(
        x_correlation_id=x_correlation_id,
        x_insz=x_insz,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_correlation_id: UUID,
    x_insz: str,
) -> ErrorMessage | JsonLdRoot | None:
    """Dienstverlening informatie opvragen.

     Vraag alle informatie op over een Dienstverlening tussen Organisaties en Personen zoals een
    Activeringstraject van een Werkzoekende door de Organisatie VDAB. Iedere Dienstverlening tussen
    Organisatie - Personen heeft zijn eigen ID.

    Args:
        x_correlation_id (UUID):
        x_insz (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | JsonLdRoot
    """

    return sync_detailed(
        client=client,
        x_correlation_id=x_correlation_id,
        x_insz=x_insz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_correlation_id: UUID,
    x_insz: str,
) -> Response[ErrorMessage | JsonLdRoot]:
    """Dienstverlening informatie opvragen.

     Vraag alle informatie op over een Dienstverlening tussen Organisaties en Personen zoals een
    Activeringstraject van een Werkzoekende door de Organisatie VDAB. Iedere Dienstverlening tussen
    Organisatie - Personen heeft zijn eigen ID.

    Args:
        x_correlation_id (UUID):
        x_insz (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | JsonLdRoot]
    """

    kwargs = _get_kwargs(
        x_correlation_id=x_correlation_id,
        x_insz=x_insz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_correlation_id: UUID,
    x_insz: str,
) -> ErrorMessage | JsonLdRoot | None:
    """Dienstverlening informatie opvragen.

     Vraag alle informatie op over een Dienstverlening tussen Organisaties en Personen zoals een
    Activeringstraject van een Werkzoekende door de Organisatie VDAB. Iedere Dienstverlening tussen
    Organisatie - Personen heeft zijn eigen ID.

    Args:
        x_correlation_id (UUID):
        x_insz (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | JsonLdRoot
    """

    return (
        await asyncio_detailed(
            client=client,
            x_correlation_id=x_correlation_id,
            x_insz=x_insz,
        )
    ).parsed
