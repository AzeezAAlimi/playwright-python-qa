import pytest
import json
from api.auth_client import AuthClient
from conftest import auth_client
from test_data.test_user_detail import TEST_USER


@pytest.mark.asyncio(loop_scope="session")
async def test_login(
        auth_client: AuthClient,
):
    auth_response = await auth_client.login(
        surname=TEST_USER["surname"],
        given_name=TEST_USER["given_name"],
        national_personal_id=TEST_USER["national_personal_id"],
        personal_id_type=TEST_USER["personal_id_type"]
    )
    assert auth_response.status == 200
    assert auth_response.ok
    auth_response_body = await auth_response.json()
    print(json.dumps(auth_response_body, indent=2))
    assert "token" in auth_response_body
    assert isinstance(auth_response_body["token"], str)
    assert auth_response_body["token"]
    token = auth_response_body["token"]

# python -m pytest tests/api/reusable_api_classes/test_auth_client.py -s
