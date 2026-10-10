import pytest
import json
from playwright.async_api import APIRequestContext
from test_data.profile_data import VALID_PROFILE
from config.setting import BASE_URL_STAGE

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_profile(
        api_request_context: APIRequestContext,
        auth_token: str
):
    put_profile_response = await api_request_context.put(
        f"{BASE_URL_STAGE}/api/directory2/v1/users/me/profile",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
        data={
                "userContactInformation": {
                    "email": VALID_PROFILE["email"],
                    "mobile_number": VALID_PROFILE["mobile_number"],
                }
            },
    )
    assert put_profile_response.status == 200
    put_profile_response_body = await put_profile_response.json()
    print(json.dumps(put_profile_response_body, indent=2))
    assert "mobileNumber" in put_profile_response_body["userProfile"]
    assert isinstance(put_profile_response_body["userProfile"]["mobileNumber"], str)
    assert put_profile_response_body["userProfile"]["mobileNumber"] == "+46739376571"
    assert "email" in put_profile_response_body["userProfile"]
    assert isinstance(put_profile_response_body["userProfile"]["email"], str)
    assert put_profile_response_body["userProfile"]["email"] == "renandstimpy@gmail.com"


    get_updated_profile_response = await api_request_context.get(
        f"{BASE_URL_STAGE}/api/directory2/v1/users/me/profile",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    )
    assert get_updated_profile_response.status == 200
    get_updated_profile_response_body = await get_updated_profile_response.json()
    print(json.dumps(get_updated_profile_response_body, indent=2))
    assert "mobileNumber" in get_updated_profile_response_body["userProfile"]
    assert isinstance(get_updated_profile_response_body["userProfile"]["mobileNumber"], str)
    assert get_updated_profile_response_body["userProfile"]["mobileNumber"] == "+46739376571"
    assert "email" in get_updated_profile_response_body["userProfile"]
    assert isinstance(get_updated_profile_response_body["userProfile"]["email"], str)
    assert get_updated_profile_response_body["userProfile"]["email"] == "renandstimpy@gmail.com"

# python -m pytest tests/api/positive/test_profile.py -s