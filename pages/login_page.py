from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.test_login_button = page.get_by_role(
            "button",
            name="Test login"
        )

        self.personal_number_input = page.get_by_role(
            "textbox",
            name="Personnummer Prefill test personal number"
        )

        self.test_logga_in_button = page.get_by_role(
            "button",
            name="Test Logga in"
        )

        self.invalid_personal_number_alert = (page.get_by_role(
            "alert").filter(
            has_text="Felaktigt personnummer"))

    async def open_test_login(self):
        await self.test_login_button.click()

    async def login_with_personal_number(self, personal_number: str):
        await self.personal_number_input.fill(personal_number)
        await self.test_logga_in_button.click()

    async def enter_invalid_personal_number(self, personal_number: str):
        await self.personal_number_input.fill(personal_number)