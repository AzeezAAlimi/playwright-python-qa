import pytest
import json
from playwright.async_api import APIRequestContext
from test_data.health_data_1 import HEALTH_DATA_1
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
    patient_id = get_user_response_body["patient"]["id"]


    put_health_data_response = await api_request_context.put(
        f"{BASE_URL_STAGE}/api/healthmanager/v1/healthprofiles/{patient_id}",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
        data={
            "weight": HEALTH_DATA_1["weight"],
            "height": HEALTH_DATA_1["height"],
            "allergies": HEALTH_DATA_1["allergies"],
            "diagnoses": HEALTH_DATA_1["diagnoses"],
            "surgery": HEALTH_DATA_1["surgery"],
            "medication": HEALTH_DATA_1["medication"]
        },
    )
    assert put_health_data_response.status == 200


    get_health_data_response = await api_request_context.get(
        f"{BASE_URL_STAGE}/api/healthmanager/v1/healthprofiles/{patient_id}",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    )
    assert get_health_data_response.status == 200
    get_health_data_response_body = await get_health_data_response.json()
    print(json.dumps(get_health_data_response_body, indent=2))
    assert "id" in get_health_data_response_body
    assert isinstance(get_health_data_response_body["id"], str)
    assert get_health_data_response_body["id"]
    assert "height" in get_health_data_response_body
    assert isinstance(get_health_data_response_body["height"], int)
    assert get_health_data_response_body["height"]

# python -m pytest tests/api/positive/test_health_data.py -s