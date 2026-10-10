import pytest
import pytest_asyncio
from pathlib import Path
from config.setting import BASE_URL_STAGE
from test_data.users import VALID_PERSONAL_NUMBER_STAGE
from playwright.async_api import Browser, expect, APIRequestContext, Playwright
from pages.home_page import HomePage
from pages.login_page import LoginPage
from api.profile_client import ProfileClient
from api.health_client import HealthClient
from api.auth_client import AuthClient
from test_data.test_user_detail import TEST_USER
from test_data.profile_data import VALID_PROFILE
from config.setting import BASE_URL_STAGE


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def auth_state(browser: Browser):
    context = await browser.new_context()
    page = await context.new_page()

    home_page = HomePage(page)
    login_page = LoginPage(page)

    await home_page.open()
    await home_page.accept_cookies()
    await home_page.go_to_login()

    await expect(page).to_have_url(f"{BASE_URL_STAGE}/home-login")

    await login_page.open_test_login()

    await login_page.login_with_personal_number(VALID_PERSONAL_NUMBER_STAGE)

    await page.wait_for_url(f"{BASE_URL_STAGE}/home")

    await page.context.storage_state(
        path="auth/storage_state.json"
    )

    await context.close()

    return "auth/storage_state.json"


@pytest_asyncio.fixture(loop_scope="session")
async def authenticated_page(
        browser: Browser,
        auth_state: str,
        request
):

    context = await browser.new_context(
        storage_state=auth_state
    )

    await context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = await context.new_page()

    yield page

    Path("traces").mkdir(exist_ok=True)
    Path("screenshots").mkdir(exist_ok=True)

    test_name = request.node.name

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        await page.screenshot(
            path=f"screenshots/{test_name}.png",
            full_page=True
        )

    await context.tracing.stop(
        path=f"traces/{test_name}.zip"
    )

    await context.close()


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def api_request_context(
    playwright: Playwright,
):
    request_context = await playwright.request.new_context(
        base_url=BASE_URL_STAGE
    )

    yield request_context

    await request_context.dispose()


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def auth_token(
        api_request_context: APIRequestContext
):
    get_auth_response = await api_request_context.post(
        f"{BASE_URL_STAGE}/api/test/login?guest=false",
        data={
            "surname": TEST_USER["surname"],
            "givenName": TEST_USER["given_name"],
            "nationalPersonalId": TEST_USER["national_personal_id"],
            "personalIdType": TEST_USER["personal_id_type"],
        },
    )
    assert get_auth_response.status == 200
    get_auth_response_body = await get_auth_response.json()
    assert "token" in get_auth_response_body
    assert get_auth_response_body["token"]
    return get_auth_response_body["token"]


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def profile_client(
    api_request_context: APIRequestContext,
    auth_token: str
):
    return ProfileClient(
        api_request_context,
        auth_token
    )


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def health_client(
    api_request_context: APIRequestContext,
    auth_token: str
):
    return HealthClient(
        api_request_context,
        auth_token
    )


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def auth_client(
    api_request_context: APIRequestContext
):
    return AuthClient(api_request_context)


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def patient_id(
    api_request_context: APIRequestContext,
    auth_token: str
):
    response = await api_request_context.get(
        "/api/directory2/v1/users/me",
        headers={
            "Authorization": f"Bearer {auth_token}"
        },
    )
    assert response.status == 200
    body = await response.json()
    return body["patient"]["id"]