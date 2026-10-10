from playwright.async_api import Page

from components.navigation_bar import NavigationBar

class MyTaskPage:
    def __init__(self, page: Page):
        self.page = page

        self.case_tab = page.get_by_role(
            "button",
            name="Ärenden",
            exact=True
        )

        self.closed_case_button = page.get_by_role(
            "button",
            name="Avslutade ärenden",
            exact=True
        )

        self.ongoing_case_button = page.get_by_role(
            "button",
            name="ågående ärenden"
        )

        self.message_tab = page.get_by_role(
            "button",
            name="Meddelanden"
        )

        self.no_pending_case_text = page.get_by_role(
            "heading",
            name="Du har inga pågående ärenden"
        )

        self.no_closed_case_text = page.get_by_role(
            "heading",
            name="Du har inga avslutade ärenden"
        )

        self.active_tab = page.get_by_role(
            "button",
            name="Aktiva"
        )

        self.completed_tab = page.get_by_role(
            "button",
            name="Avslutade"
        )

        self.active_text = page.get_by_role(
            "heading",
            name="Du har inga pågående ärenden"
        )

        self.completed_text = page.get_by_role(
            "heading",
            name="Du har inga avslutade ärenden"
        )

        self.nav_bar = NavigationBar(page)

    async def open_cases_tab(self):
        await self.case_tab.click()

    async def open_closed_cases(self):
        await self.closed_case_button.click()

    async def open_ongoing_cases(self):
        await self.ongoing_case_button.click()

    async def open_message_tab(self):
        await self.message_tab.click()

    async def open_active_tab(self):
        await self.active_tab.click()

    async def open_completed_tab(self):
        await self.completed_tab.click()