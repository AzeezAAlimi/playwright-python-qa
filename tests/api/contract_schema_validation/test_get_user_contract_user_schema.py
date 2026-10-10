import json
import pytest
from jsonschema import validate
from tests.api.contract_schema_validation.schemas.user_schema import USER_SCHEMA
from playwright.async_api import APIRequestContext


@pytest.mark.smoke
@pytest.mark.api
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

    validate(
        instance=body,
        schema=USER_SCHEMA
    )

# python -m pytest tests/api/contract_schema_validation/test_get_user_contract_user_schema.py -s