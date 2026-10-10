import pytest
import json
from playwright.async_api import APIRequestContext
from config.setting import BASE_URL_STAGE


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_health_data_empty_payload(
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
    patient_id = get_user_response_body["patient"]["id"]


    put_health_data_response = await api_request_context.put(
        f"{BASE_URL_STAGE}/api/healthmanager/v1/healthprofiles/{patient_id}",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    )
    print("Status:", put_health_data_response.status)
    print("Body:", await put_health_data_response.text())
    assert put_health_data_response.status == 400
    put_health_data_response_body = await put_health_data_response.json()
    assert put_health_data_response_body["status"] == 400
    assert put_health_data_response_body["error"] == "Bad Request"

# python -m pytest tests/api/negative/test_health_data_negative.py -s