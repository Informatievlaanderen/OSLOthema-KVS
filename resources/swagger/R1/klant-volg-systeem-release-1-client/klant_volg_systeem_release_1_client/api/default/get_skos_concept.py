from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_ld_root import JsonLdRoot
from ...types import Response


def _get_kwargs(
    conceptscheme: str,
    concept: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/id/concept/{conceptscheme}/{concept}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> JsonLdRoot | None:
    if response.status_code == 200:
        response_200 = JsonLdRoot.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[JsonLdRoot]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conceptscheme: str,
    concept: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[JsonLdRoot]:
    """
    Args:
        conceptscheme (str):
        concept (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonLdRoot]
    """

    kwargs = _get_kwargs(
        conceptscheme=conceptscheme,
        concept=concept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conceptscheme: str,
    concept: str,
    *,
    client: AuthenticatedClient | Client,
) -> JsonLdRoot | None:
    """
    Args:
        conceptscheme (str):
        concept (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsonLdRoot
    """

    return sync_detailed(
        conceptscheme=conceptscheme,
        concept=concept,
        client=client,
    ).parsed


async def asyncio_detailed(
    conceptscheme: str,
    concept: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[JsonLdRoot]:
    """
    Args:
        conceptscheme (str):
        concept (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonLdRoot]
    """

    kwargs = _get_kwargs(
        conceptscheme=conceptscheme,
        concept=concept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conceptscheme: str,
    concept: str,
    *,
    client: AuthenticatedClient | Client,
) -> JsonLdRoot | None:
    """
    Args:
        conceptscheme (str):
        concept (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsonLdRoot
    """

    return (
        await asyncio_detailed(
            conceptscheme=conceptscheme,
            concept=concept,
            client=client,
        )
    ).parsed
