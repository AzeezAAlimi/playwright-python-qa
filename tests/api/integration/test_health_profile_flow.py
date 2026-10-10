import pytest
import json
from playwright.async_api import APIRequestContext
from test_data.health_data_2 import HEALTH_DATA_2
from config.setting import BASE_URL_STAGE


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_integration_health_data(
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
            "Authorization": f"Bearer {auth_token}"
        },
        data={
            "weight": HEALTH_DATA_2["weight"],
            "height": HEALTH_DATA_2["height"],
            "allergies": HEALTH_DATA_2["allergies"],
            "diagnoses": HEALTH_DATA_2["diagnoses"],
            "surgery": HEALTH_DATA_2["surgery"],
            "medication": HEALTH_DATA_2["medication"]
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
    assert get_health_data_response_body["weight"] == 80
    assert get_health_data_response_body["height"] == 198
    assert get_health_data_response_body["allergies"] == "Arsenal are the best team"
    assert get_health_data_response_body["diagnoses"] == "Arsenal won the league"
    assert get_health_data_response_body["surgery"] == "Arsenal are going to win the league"
    assert get_health_data_response_body["medication"] == "Arsenal are going to win the champions league"

# python -m pytest tests/api/integration/test_health_profile_flow.py -s