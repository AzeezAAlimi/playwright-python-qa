import pytest
from playwright.async_api import APIRequestContext
from test_data.test_user_detail import TEST_USER
from config.setting import BASE_URL_STAGE


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_login_missing_personal_id(
        api_request_context: APIRequestContext
):
    post_auth_response = await api_request_context.post(
        f"{BASE_URL_STAGE}/api/test/login?guest=false",
        data={
            "surname": TEST_USER["surname"],
            "givenName": TEST_USER["given_name"],
            "personalIdType": TEST_USER["personal_id_type"],
        },
    )
    print("Status:", post_auth_response.status)
    print("Body:", await post_auth_response.text())
    assert post_auth_response.status == 400
    post_auth_response_body = await post_auth_response.json()
    assert post_auth_response_body["message"] == "invalid patient data, the following required fields are null: externalId, authenticationKey"


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_login_missing_surname_given_name(
        api_request_context: APIRequestContext
):
    post_auth_response = await api_request_context.post(
        f"{BASE_URL_STAGE}/api/test/login?guest=false",
        data={
            "nationalPersonalId": TEST_USER["national_personal_id"],
            "personalIdType": TEST_USER["personal_id_type"],
        },
    )
    print("Status:", post_auth_response.status)
    print("Body:", await post_auth_response.text())
    assert post_auth_response.status == 400
    post_auth_response_body = await post_auth_response.json()
    assert post_auth_response_body["message"] == "invalid patient data, the following required fields are null: givenName, surname"


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_login_empty_payload(
        api_request_context: APIRequestContext
):
    post_auth_response = await api_request_context.post(
        f"{BASE_URL_STAGE}/api/test/login?guest=false",
    )
    print("Status:", post_auth_response.status)
    print("Body:", await post_auth_response.text())
    assert post_auth_response.status == 400
    post_auth_response_body = await post_auth_response.json()
    assert post_auth_response_body["message"] == "RESTEASY003200: Could not find message body reader for type: class se.platform24.patient.auth.test.dto.TestLoginRequestDTO of content type: */*"

# python -m pytest tests/api/negative/test_auth_negative.py -s