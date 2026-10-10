import pytest
from playwright.async_api import APIRequestContext
from test_data.profile_data_incorrect_email import INVALID_EMAIL_PROFILE
from test_data.profile_data_incorrect_number import INVALID_NUMBER_PROFILE
from config.setting import BASE_URL_STAGE


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_profile_empty_payload(
        api_request_context: APIRequestContext,
        auth_token: str
):
    put_profile_response = await api_request_context.put(
        f"{BASE_URL_STAGE}/api/directory2/v1/users/me/profile",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    )
    print("Status:", put_profile_response.status)
    print("Body:", await put_profile_response.text())
    assert put_profile_response.status == 500
    put_profile_response_body = await put_profile_response.json()
    assert put_profile_response_body["message"] == "unknown error"


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_profile_incorrect_email_format(
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
                "email": INVALID_EMAIL_PROFILE["email"],
                "mobileNumber": INVALID_EMAIL_PROFILE["mobileNumber"],
            }
        },
    )
    print("Status:", put_profile_response.status)
    print("Body:", await put_profile_response.text())
    assert put_profile_response.status == 400
    put_profile_response_body = await put_profile_response.json()
    assert put_profile_response_body["title"] == "Constraint Violation"
    assert put_profile_response_body["status"] == 400
    assert put_profile_response_body["violations"][0]["field"] == "updateProfile.updateProfileDTO.userContactInformation.email"
    assert put_profile_response_body["violations"][0]["message"] == "must be a well-formed email address"


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_profile_incorrect_phone_number_format(
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
                "email": INVALID_NUMBER_PROFILE["email"],
                "mobileNumber": INVALID_NUMBER_PROFILE["mobileNumber"],
            }
        },
    )
    print("Status:", put_profile_response.status)
    print("Body:", await put_profile_response.text())
    assert put_profile_response.status == 400
    put_profile_response_body = await put_profile_response.json()
    assert put_profile_response_body["message"] == "unable to update person with patient id 828968cb-4ace-46e8-9b3c-449d6e27cbc6 due to invalid data: errors=[update person error: invalid phone number]"

# python -m pytest tests/api/negative/test_profile_negative.py -s