import pytest
from playwright.async_api import APIRequestContext
from conftest import api_request_context, auth_token
from test_data.profile_data import VALID_PROFILE


@pytest.mark.asyncio(loop_scope="session")
async def test_profile_update_is_idempotent(
    api_request_context: APIRequestContext,
    auth_token: str
):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    payload = {
        "userContactInformation": {
            "email": VALID_PROFILE["email"],
            "mobile_number": VALID_PROFILE["mobile_number"],
        }
    }

    first_response = await api_request_context.put(
        "/api/directory2/v1/users/me/profile",
        headers=headers,
        data=payload,
    )

    second_response = await api_request_context.put(
        "/api/directory2/v1/users/me/profile",
        headers=headers,
        data=payload,
    )

    assert first_response.status == 200
    assert second_response.status == 200

    get_response = await api_request_context.get(
        "/api/directory2/v1/users/me/profile",
        headers=headers,
    )

    assert get_response.status == 200
    body = await get_response.json()

    assert body["userProfile"]["email"] == "renandstimpy@gmail.com"
    assert body["userProfile"]["mobileNumber"] == "+46739376571"

# python -m pytest tests/api/contract_schema_validation/test_profile_contract_schema.py --headed -s