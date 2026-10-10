from playwright.async_api import Page

class NavigationBar:
    def __init__(self, page: Page):
        self.page = page
        self.home_navigation_button = page.get_by_role("navigation", name="Meny").get_by_role("link", name="Hem")
        self.cases_navigation_button = page.get_by_role("navigation", name="Meny").get_by_role("link", name="Ärenden ")
        self.my_profile_navigation_button = page.get_by_role("navigation", name="Meny").get_by_role("link", name="Min profil")
        self.support_navigation_button = page.get_by_role("navigation", name="Meny").get_by_role("link", name="Support")

    async def go_to_home(self):
        await self.home_navigation_button.click()

    async def go_to_cases(self):
        await self.cases_navigation_button.click()

    async def go_to_my_profile(self):
        await self.my_profile_navigation_button.click()

    async def go_to_support(self):
        await self.support_navigation_button.click()