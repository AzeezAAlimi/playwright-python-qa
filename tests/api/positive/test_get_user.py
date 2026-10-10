import pytest
import json
from playwright.async_api import APIRequestContext
from config.setting import BASE_URL_STAGE

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_get_user(
        api_request_context: APIRequestContext,
        auth_token: str
):
    get_user_response = await api_request_context.get(
        f"{BASE_URL_STAGE}/api/directory2/v1/users/me",
        headers={
            "Authorization": f"Bearer {auth_token}"
        },
    )
    assert get_user_response.status == 200
    get_user_response_body = await get_user_response.json()
    print(json.dumps(get_user_response_body, indent=2))
    assert "username" in get_user_response_body
    assert isinstance(get_user_response_body["username"], str)
    assert get_user_response_body["username"]
    assert "id" in get_user_response_body["patient"]
    assert isinstance(get_user_response_body["patient"]["id"], str)
    assert get_user_response_body["patient"]["id"]

# python -m pytest tests/api/positive/test_get_user.py -s