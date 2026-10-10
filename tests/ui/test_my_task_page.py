import pytest
from config.setting import BASE_URL_STAGE
from playwright.async_api import Page, expect
from pages.home_page import HomePage
from pages.my_task_page import MyTaskPage


@pytest.mark.smoke
@pytest.mark.tasks
@pytest.mark.asyncio(loop_scope="session")
async def test_active_tab(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_task_page = MyTaskPage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")
    await home_page.nav_bar.go_to_cases()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/active")
    await expect(my_task_page.active_tab).to_be_visible()
    await my_task_page.open_active_tab()
    await expect(my_task_page.active_text).to_be_visible()


@pytest.mark.smoke
@pytest.mark.tasks
@pytest.mark.asyncio(loop_scope="session")
async def test_completed_tab(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_task_page = MyTaskPage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")
    await home_page.nav_bar.go_to_cases()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/active")
    await expect(my_task_page.completed_tab).to_be_visible()
    await my_task_page.open_completed_tab()
    await expect(my_task_page.completed_text).to_be_visible()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/finished")



@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.tasks
@pytest.mark.asyncio(loop_scope="session")
async def test_cases_tab_dev(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_task_page = MyTaskPage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")
    await home_page.nav_bar.go_to_cases()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/active")
    await expect(my_task_page.case_tab).to_be_visible()
    await my_task_page.case_tab.click()
    await expect(my_task_page.no_pending_case_text).to_be_visible()
    await expect(my_task_page.closed_case_button).to_be_visible()
    await my_task_page.open_closed_cases()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/finished")
    await expect(my_task_page.no_closed_case_text).to_be_visible()
    await expect(my_task_page.ongoing_case_button).to_be_visible()
    await my_task_page.ongoing_case_button.click()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/active")


@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.tasks
@pytest.mark.asyncio(loop_scope="session")
async def test_messages_tab_dev(authenticated_page: Page):
    page = authenticated_page

    home_page = HomePage(page)
    my_task_page = MyTaskPage(page)

    await page.goto(f"{BASE_URL_STAGE}/home")
    await home_page.nav_bar.go_to_cases()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/active")
    await expect(my_task_page.message_tab).to_be_visible()
    await my_task_page.message_tab.click()
    await expect(page).to_have_url(f"{BASE_URL_STAGE}/history/messages")

# python -m pytest tests/ui/test_my_task_page.py --headed -s
# python -m pytest -m smoke
# python -m pytest -m tasks
# python -m pytest -m "smoke and tasks"