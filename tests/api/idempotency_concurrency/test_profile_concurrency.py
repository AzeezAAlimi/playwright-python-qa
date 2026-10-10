import pytest
import asyncio
from playwright.async_api import APIRequestContext
from conftest import api_request_context, auth_token
from test_data.profile_data import VALID_PROFILE


@pytest.mark.asyncio(loop_scope="session")
async def test_profile_concurrent_updates(
    api_request_context: APIRequestContext,
    auth_token: str
):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    payload_one = {
        "userContactInformation": {
            "email": VALID_PROFILE["email"],
            "mobile_number": VALID_PROFILE["mobile_number"],
        }
    }

    payload_two = {
        "userContactInformation": {
            "email": VALID_PROFILE["email"],
            "mobile_number": VALID_PROFILE["mobile_number"],
        }
    }

    first_response, second_response = await asyncio.gather(
        api_request_context.put(
            "/api/directory2/v1/users/me/profile",
            headers=headers,
            data=payload_one,
        ),
        api_request_context.put(
            "/api/directory2/v1/users/me/profile",
            headers=headers,
            data=payload_two,
        ),
    )

    print("First status:", first_response.status)
    print("Second status:", second_response.status)

    get_response = await api_request_context.get(
        "/api/directory2/v1/users/me/profile",
        headers=headers,
    )

    assert get_response.status == 200

    body = await get_response.json()

    print("Final email:", body["userProfile"]["email"])

# python -m pytest tests/api/idempotency_concurrency/test_profile_concurrency.py --headed -s