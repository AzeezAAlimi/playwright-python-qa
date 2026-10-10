from playwright.async_api import APIRequestContext


class HealthClient:
    def __init__(
        self,
        api_request_context: APIRequestContext,
        auth_token: str
    ):
        self.api_request_context = api_request_context
        self.headers = {
            "Authorization": f"Bearer {auth_token}"
        }

    async def get_health_profile(self, patient_id: str):
        return await self.api_request_context.get(
            f"/api/healthmanager/v1/healthprofiles/{patient_id}",
            headers=self.headers,
        )

    async def update_health_profile(
        self,
        patient_id: str,
        data: dict
    ):
        return await self.api_request_context.put(
            f"/api/healthmanager/v1/healthprofiles/{patient_id}",
            headers=self.headers,
            data=data,
        )