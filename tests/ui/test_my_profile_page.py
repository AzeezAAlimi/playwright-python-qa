import re
import pytest
from config.setting import BASE_URL_STAGE
from test_data.contact_details import USER_1_PHONE_NUMBER, USER_1_EMAIL
from playwright.async_api import Page, expect
from pages.home_page import HomePage
from pages.my_profile_page import MyProfilePage


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.profile
@pytest.mark.asyncio(loop_scope="session")
async def test_my_profile_logout(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")

    await home_page.nav_bar.go_to_my_profile()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")
    await page.get_by_test_id("timezone-notification").get_by_role(
    "button",
    name="Stäng").click()
    await expect(my_profile_page.logout_button).to_be_visible()
    await my_profile_page.logout()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/home")


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.profile
@pytest.mark.asyncio(loop_scope="session")
async def test_my_care_plan_menu(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")

    await home_page.nav_bar.go_to_my_profile()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")
    await page.get_by_test_id("timezone-notification").get_by_role(
    "button",
    name="Stäng").click()
    await expect(my_profile_page.my_care_plan_menu).to_be_visible()
    await my_profile_page.open_my_care_plan()
    await expect(my_profile_page.header_bar.close_button).to_be_visible()
    await my_profile_page.header_bar.click_close()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/home")


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.profile
@pytest.mark.asyncio(loop_scope="session")
async def test_health_data_menu(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")

    await home_page.nav_bar.go_to_my_profile()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")
    await page.get_by_test_id("timezone-notification").get_by_role(
    "button",
    name="Stäng").click()
    await expect(my_profile_page.health_data_menu).to_be_visible()
    await my_profile_page.open_health_data()
    await expect(my_profile_page.header_bar.back_button).to_be_visible()
    await my_profile_page.header_bar.click_back()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.profile
@pytest.mark.asyncio(loop_scope="session")
async def test_vaccinations_menu(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")

    await home_page.nav_bar.go_to_my_profile()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")
    await page.get_by_test_id("timezone-notification").get_by_role(
    "button",
    name="Stäng").click()
    await expect(
        my_profile_page.vaccinations_menu
    ).to_be_visible()
    await my_profile_page.open_vaccinations()

    await expect(
        my_profile_page.header_bar.back_button
    ).to_be_visible()

    await expect(
        my_profile_page.book_directly_button
    ).to_be_visible()

    new_tab = await my_profile_page.open_vaccination_booking()
    await new_tab.wait_for_load_state()
    await expect(new_tab).to_have_url(
        re.compile(r"^https://doktor24\.se/tjanster/vaccin/")
    )
    await new_tab.close()
    await my_profile_page.header_bar.click_back()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.profile
@pytest.mark.asyncio(loop_scope="session")
async def test_edit_contact_details_menu(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")

    await home_page.nav_bar.go_to_my_profile()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")
    await page.get_by_test_id("timezone-notification").get_by_role(
    "button",
    name="Stäng").click()
    await expect(my_profile_page.contact_details_menu).to_be_visible()
    await my_profile_page.update_contact_details(USER_1_PHONE_NUMBER, USER_1_EMAIL)
    await my_profile_page.header_bar.click_back()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")


@pytest.mark.regression
@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.profile
@pytest.mark.asyncio(loop_scope="session")
async def test_consent_menu(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_profile_page = MyProfilePage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")

    await home_page.nav_bar.go_to_my_profile()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")
    await page.get_by_test_id("timezone-notification").get_by_role(
    "button",
    name="Stäng").click()
    await expect(my_profile_page.consent_menu).to_be_visible()
    await my_profile_page.open_consent()
    await expect(my_profile_page.consent_medical_history_switch).to_be_checked(checked=True)
    await expect(my_profile_page.consent_medication_list_switch).to_be_checked(checked=True)
    await my_profile_page.header_bar.click_back()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/aboutyou")

# python -m pytest tests/ui/test_my_profile_page.py --headed -s
# python -m pytest -m smoke
# python -m pytest -m profile
# python -m pytest -m "smoke and profile"