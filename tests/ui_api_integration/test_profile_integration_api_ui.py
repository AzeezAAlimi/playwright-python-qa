import pytest
from playwright.async_api import Page, expect

from api.profile_client import ProfileClient
from pages.home_page import HomePage
from pages.my_profile_page import MyProfilePage
from config.setting import BASE_URL_STAGE

@pytest.mark.asyncio(loop_scope="session")
async def test_profile_update_via_api_visible_in_ui(
        authenticated_page: Page,
        profile_client: ProfileClient,
):
    page = authenticated_page
    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    expected_email = "renandstimpy@gmail.com"
    expected_mobile = "739376571"

    put_response = await profile_client.update_profile(
        email=expected_email,
        mobile_number=expected_mobile,
    )

    assert put_response.status == 200

    await page.goto(f"{BASE_URL_STAGE}/home")
    await home_page.nav_bar.go_to_my_profile()

    await expect(page).to_have_url(
        f"{BASE_URL_STAGE}/aboutyou"
    )

    await expect(
        my_profile_page.contact_details_menu
    ).to_be_visible()

    await my_profile_page.contact_details_menu.click()

    await expect(my_profile_page.contact_details_email_input).to_have_value(expected_email)
    await expect(my_profile_page.contact_details_phone_number_input).to_have_value(expected_mobile)

    await page.pause()

# python -m pytest tests/ui_api_integration/test_profile_integration_api_ui.py --headed -s