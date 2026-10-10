import pytest
import json
from api.profile_client import ProfileClient
from test_data.profile_data import VALID_PROFILE

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_profile(
        profile_client: ProfileClient
):
    put_profile_response = await profile_client.update_profile(
        email=VALID_PROFILE["email"],
        mobile_number=VALID_PROFILE["mobile_number"],
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


    get_updated_profile_response = await profile_client.get_profile()
    assert get_updated_profile_response.status == 200
    get_updated_profile_response_body = await get_updated_profile_response.json()
    print(json.dumps(get_updated_profile_response_body, indent=2))
    assert "mobileNumber" in get_updated_profile_response_body["userProfile"]
    assert isinstance(get_updated_profile_response_body["userProfile"]["mobileNumber"], str)
    assert get_updated_profile_response_body["userProfile"]["mobileNumber"] == "+46739376571"
    assert "email" in get_updated_profile_response_body["userProfile"]
    assert isinstance(get_updated_profile_response_body["userProfile"]["email"], str)
    assert get_updated_profile_response_body["userProfile"]["email"] == "renandstimpy@gmail.com"

# python -m pytest tests/api/reusable_api_classes/test_profile_client.py -s
