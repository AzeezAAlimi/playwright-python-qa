from playwright.async_api import Page
from config.setting import BASE_URL_STAGE
from components.navigation_bar import NavigationBar

class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.start_care_visit_button = page.get_by_test_id("call-to-action")

        self.continue_button = page.get_by_role(
            "button",
            name="Fortsätt"
        )

        self.login_link = page.get_by_role(
            "link",
            name="Logga in"
        )

        self.profile_link = page.get_by_role(
            "navigation",
            name="Start page"
        ).get_by_role(
            "link",
            name="Min profil"
        )

        self.accept_button = page.get_by_role(
            "button",
            name="Acceptera alla cookies"
        )

        self.nav_bar = NavigationBar(page)

    async def open(self):
        await self.page.goto(f"{BASE_URL_STAGE}/home")

    async def accept_cookies(self):
        if await self.accept_button.is_visible():
            await self.accept_button.click()

    async def go_to_login(self):
        await self.login_link.click()

    async def go_to_seek_care(self, personal_id: str):
        await self.start_care_visit_button.click()
        await self.page.locator(f'[value="{personal_id}"]').click()
        await self.continue_button.click()
