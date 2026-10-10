from playwright.async_api import APIRequestContext


class AuthClient:
    def __init__(
        self,
        api_request_context: APIRequestContext
    ):
        self.api_request_context = api_request_context

    async def login(
        self,
        surname: str,
        given_name: str,
        national_personal_id: str,
        personal_id_type: str
    ):
        return await self.api_request_context.post(
            "/api/test/login?guest=false",
            data={
                "surname": surname,
                "givenName": given_name,
                "nationalPersonalId": national_personal_id,
                "personalIdType": personal_id_type,
            },
        )