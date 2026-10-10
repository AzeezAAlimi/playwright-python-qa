import pytest
from playwright.async_api import Page, expect

from api.profile_client import ProfileClient
from pages.home_page import HomePage
from pages.my_profile_page import MyProfilePage
from config.setting import BASE_URL_STAGE

@pytest.mark.asyncio(loop_scope="session")
async def test_profile_update_via_ui_persists_in_api(
        authenticated_page: Page,
        profile_client: ProfileClient,
):
    page = authenticated_page
    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    expected_email = "arsenaltest@gmail.com"
    expected_mobile = "739376572"

    await page.goto(f"{BASE_URL_STAGE}/home")
    await home_page.nav_bar.go_to_my_profile()

    await expect(page).to_have_url(
        f"{BASE_URL_STAGE}/aboutyou"
    )

    await my_profile_page.update_contact_details(
        expected_mobile,
        expected_email,
    )

    await my_profile_page.contact_details_confirm_button.click()

    get_response = await profile_client.get_profile()

    assert get_response.status == 200

    body = await get_response.json()

    assert body["userProfile"]["email"] == expected_email

    await page.pause()

# python -m pytest tests/ui_api_integration/test_profile_integration_ui_api.py --headed -s