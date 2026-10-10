from playwright.async_api import APIRequestContext


class ProfileClient:
    def __init__(
        self,
        api_request_context: APIRequestContext,
        auth_token: str
    ):
        self.api_request_context = api_request_context
        self.headers = {
            "Authorization": f"Bearer {auth_token}"
        }

    async def get_profile(self):
        return await self.api_request_context.get(
            "/api/directory2/v1/users/me/profile",
            headers=self.headers,
        )

    async def update_profile(
        self,
        email: str,
        mobile_number: str
    ):
        return await self.api_request_context.put(
            "/api/directory2/v1/users/me/profile",
            headers=self.headers,
            data={
                "userContactInformation": {
                    "email": email,
                    "mobileNumber": mobile_number,
                }
            },
        )