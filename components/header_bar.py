from playwright.async_api import Page

class HeaderBar:
    def __init__(self, page: Page):
        self.page = page
        self.close_button = page.get_by_role("button", name="close")
        self.back_button = page.get_by_role("button", name="Tillbaka")

    async def click_close(self):
        await self.close_button.click()

    async def click_back(self):
        await self.back_button.click()