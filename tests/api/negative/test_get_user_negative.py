import pytest
from playwright.async_api import APIRequestContext
from config.setting import BASE_URL_STAGE


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_without_token(
        api_request_context: APIRequestContext
):
    get_user_response = await api_request_context.get(
        f"{BASE_URL_STAGE}/api/directory2/v1/users/me"
    )
    print("Status:", get_user_response.status)
    print("Body:", await get_user_response.text())
    assert get_user_response.status == 401
    get_user_response_body = await get_user_response.json()
    assert get_user_response_body["message"] == "Unauthorized"


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_invalid_bearer_token(
        api_request_context: APIRequestContext
):
    get_user_response = await api_request_context.get(
        f"{BASE_URL_STAGE}/api/directory2/v1/users/me",
        headers={
            "Authorization": "Bearer invalid_bearer"
        },
    )
    print("Status:", get_user_response.status)
    print("Body:", await get_user_response.text())
    assert get_user_response.status == 401
    get_user_response_body = await get_user_response.json()
    assert get_user_response_body["message"] == "Bad token; invalid JSON"

# python -m pytest tests/api/negative/test_get_user_negative.py -s