import pytest
import json
from api.health_client import HealthClient
from test_data.health_data_1 import HEALTH_DATA_1


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user(
        health_client: HealthClient,
        patient_id: str,
):
    put_health_data_response = await health_client.update_health_profile(
        patient_id=patient_id,
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


    get_health_data_response = await health_client.get_health_profile(
        patient_id=patient_id,
    )
    assert get_health_data_response.status == 200
    assert get_health_data_response.status == 200
    get_health_data_response_body = await get_health_data_response.json()
    print(json.dumps(get_health_data_response_body, indent=2))
    assert "id" in get_health_data_response_body
    assert isinstance(get_health_data_response_body["id"], str)
    assert get_health_data_response_body["id"]
    assert "height" in get_health_data_response_body
    assert isinstance(get_health_data_response_body["height"], int)
    assert get_health_data_response_body["height"]

# python -m pytest tests/api/reusable_api_classes/test_health_data_client.py -s