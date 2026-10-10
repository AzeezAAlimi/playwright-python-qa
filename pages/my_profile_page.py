from playwright.async_api import Page

from components.navigation_bar import NavigationBar

from components.header_bar import HeaderBar

class MyProfilePage:
    def __init__(self, page: Page):
        self.page = page

        self.my_care_plan_menu = page.get_by_role(
            "link",
            name="Min vårdplan"
        )

        self.health_data_menu = page.get_by_role(
            "link",
            name="Hälsodata"
        )

        self.vaccinations_menu = page.get_by_role(
            "link",
            name="Vaccinationer"
        )

        self.book_directly_button = page.get_by_role(
            "button",
            name="Boka direkt"
        )

        self.contact_details_menu = page.get_by_role(
            "link",
            name="Kontaktuppgifter"
        )

        self.contact_details_phone_number_input = page.get_by_role(
            "textbox",
            name="Mobiltelefon"
        )

        self.contact_details_email_input = page.get_by_role(
            "textbox",
            name="E-post (obligatoriskt)"
        )

        self.contact_details_confirm_button = page.get_by_role(
            "button",
            name="Bekräfta"
        )

        self.consent_menu = page.get_by_role(
            "link",
            name="Samtycken"
        )

        self.consent_medical_history_switch = page.get_by_role(
            "checkbox",
            name="Din sjukvårdshistorik"
        )

        self.consent_medication_list_switch = page.get_by_role(
            "checkbox",
            name="Din läkemedelslista"
        )

        self.logout_button = page.get_by_role(
            "button",
            name="Logga ut"
        )

        self.nav_bar = NavigationBar(page)

        self.header_bar = HeaderBar(page)

    async def open_my_care_plan(self):
        await self.my_care_plan_menu.click()

    async def open_health_data(self):
        await self.health_data_menu.click()

    async def open_vaccinations(self):
        await self.vaccinations_menu.click()

    async def open_vaccination_booking(self):
        async with self.page.expect_popup() as popup_info:
            await self.book_directly_button.click()
        return await popup_info.value

    async def update_contact_details(self, phone_number: str, email: str):
        await self.contact_details_menu.click()
        await self.contact_details_phone_number_input.fill(phone_number)
        await self.contact_details_email_input.fill(email)
        await self.contact_details_confirm_button.click()

    async def open_consent(self):
        await self.consent_menu.click()

    async def logout(self):
        await self.logout_button.click()