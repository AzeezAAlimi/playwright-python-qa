import pytest
from playwright.async_api import Page, Route

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.asyncio(loop_scope="session")
async def test_user_api_500_error(
        authenticated_page: Page
):
    page = authenticated_page

    async def mock_user_api(route: Route):
        print("Mock hit")

        await route.fulfill(
                status=500,
                content_type="application/json",
                body='{"message":"Internal Server Error"}'
        )

    await page.route(
        "**/api/directory2/v1/users/me",
        mock_user_api
    )

    await page.goto(
        "https://doktor24.app.staging.platform24.se/home"
    )

    await page.pause()


@pytest.mark.asyncio(loop_scope="session")
async def test_user_api_network_failure(
        authenticated_page: Page
):
    page = authenticated_page

    async def abort_user_api(route: Route):
        print("REQUEST ABORTED")
        await route.abort()

    await page.route(
        "**/api/directory2/v1/users/me",
        abort_user_api
    )

    await page.goto(
        "https://doktor24.app.staging.platform24.se/home"
    )

    await page.pause()

# python -m pytest tests/ui/error_handling/test_users_me_api_errors.py --headed -s