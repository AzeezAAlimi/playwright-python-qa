import json
import pytest
from playwright.async_api import APIRequestContext


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_contract(
    api_request_context: APIRequestContext,
    auth_token: str
):
    response = await api_request_context.get(
        "/api/directory2/v1/users/me",
        headers={
            "Authorization": f"Bearer {auth_token}"
        },
    )
    assert response.status == 200
    body = await response.json()
    print(json.dumps(body, indent=2))

    assert isinstance(body["username"], str)
    assert isinstance(body["givenName"], str)
    assert isinstance(body["surname"], str)
    assert isinstance(body["mobileNumber"], str)
    assert isinstance(body["email"], str)
    assert isinstance(body["preferredLanguage"], str)

    assert isinstance(body["patient"], dict)

    patient = body["patient"]

    assert isinstance(patient["id"], str)
    assert isinstance(patient["age"], int)
    assert isinstance(patient["birthDate"], str)
    assert isinstance(patient["gender"], str)
    assert isinstance(patient["givenName"], str)
    assert isinstance(patient["surname"], str)
    assert isinstance(patient["userRelation"], str)
    assert isinstance(patient["personExternalId"], str)
    assert isinstance(patient["secrecy"], str)

# python -m pytest tests/api/contract_schema_validation/test_get_user_contract.py -s