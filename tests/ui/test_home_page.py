import re
import pytest
from config.setting import BASE_URL_STAGE
from test_data.users import VALID_PERSONAL_NUMBER_STAGE, INVALID_PERSONAL_NUMBER, PERSONAL_NUMBER_USER_STAGE
from playwright.async_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.asyncio(loop_scope="session")
async def test_login_with_valid_user_id(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    await home_page.open()
    await home_page.accept_cookies()
    await expect(page).to_have_title("Doktor24")
    await home_page.go_to_login()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/home-login")
    await login_page.open_test_login()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/login/bankid-bypass")
    await login_page.login_with_personal_number(VALID_PERSONAL_NUMBER_STAGE)
    await page.wait_for_url(f"{BASE_URL_STAGE}/home")
    await expect(home_page.nav_bar.home_navigation_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.asyncio(loop_scope="session")
async def test_login_with_invalid_user_id(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    await home_page.open()
    await home_page.accept_cookies()
    await expect(page).to_have_title("Doktor24")
    await home_page.go_to_login()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/home-login")
    await login_page.open_test_login()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/login/bankid-bypass")
    await login_page.enter_invalid_personal_number(INVALID_PERSONAL_NUMBER)
    await expect(login_page.invalid_personal_number_alert).to_have_text("Felaktigt personnummer")


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.asyncio(loop_scope="session")
async def test_login_seek_care(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    await home_page.open()
    await home_page.accept_cookies()
    await expect(page).to_have_title("Doktor24")
    await home_page.go_to_login()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/home-login")
    await login_page.open_test_login()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/login/bankid-bypass")
    await login_page.login_with_personal_number(VALID_PERSONAL_NUMBER_STAGE)

    await page.wait_for_url(f"{BASE_URL_STAGE}/home")
    await home_page.go_to_seek_care(PERSONAL_NUMBER_USER_STAGE)
    await expect(page).to_have_url(re.compile(f"{BASE_URL_STAGE}/search/"))

# python -m pytest tests/ui/test_home_page.py --headed -s
# python -m pytest -m smoke
# python -m pytest -m auth
# python -m pytest -m "smoke and auth"