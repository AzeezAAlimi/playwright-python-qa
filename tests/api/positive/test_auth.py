import pytest
import json
from playwright.async_api import APIRequestContext
from test_data.test_user_detail import TEST_USER
from config.setting import BASE_URL_STAGE

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_login(
        api_request_context: APIRequestContext
):
    auth_response = await api_request_context.post(
        f"{BASE_URL_STAGE}/api/test/login?guest=false",
        data={
            "surname": TEST_USER["surname"],
            "givenName": TEST_USER["given_name"],
            "nationalPersonalId": TEST_USER["national_personal_id"],
            "personalIdType": TEST_USER["personal_id_type"],
        },
    )
    assert auth_response.status == 200
    assert auth_response.ok
    auth_response_body = await auth_response.json()
    print(json.dumps(auth_response_body, indent=2))
    assert "token" in auth_response_body
    assert isinstance(auth_response_body["token"], str)
    assert auth_response_body["token"]
    token = auth_response_body["token"]

# python -m pytest tests/api/positive/test_auth.py -s