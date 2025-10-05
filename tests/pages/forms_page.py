from __future__ import annotations

from playwright.sync_api import Locator, Page, expect


class FormsPage:
    PATH = "/bugs-form"

    def __init__(self, page: Page, base_url: str) -> None:
        self._page = page
        self._base_url = base_url.rstrip("/")

    @property
    def page(self) -> Page:
        return self._page

    @property
    def first_name_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="First Name")

    @property
    def last_name_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="Last Name")

    @property
    def phone_number_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="Enter phone number")

    @property
    def country_dropdown(self) -> Locator:
        return self._page.locator("#countries_dropdown_menu")
    
    @property
    def email_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="Enter email")
   
    @property
    def password_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="Password")
    
    @property
    def terms_and_conditions_checkbox(self) -> Locator:
        return self._page.locator("#exampleCheck1")
    @property
    def submit_button(self) -> Locator:
        return self._page.get_by_role("button", name="Register")
    @property
    def success_message_first_name(self) -> Locator:
        return self._page.locator("#resultFn")
    @property
    def success_message_last_name(self) -> Locator:
        return self._page.locator("#resultLn")
    @property
    def success_message_phone_number(self) -> Locator:
        return self._page.locator("#resultPhone")
    @property
    def success_message_country(self) -> Locator:
        return self._page.locator("#country")
    @property
    def success_message_email(self) -> Locator:
        return self._page.locator("#resultEmail")
    @property
    def success_message_password(self) -> Locator:
        return self._page.locator("#message")

    def visit(self) -> None:
        self._page.goto(f"{self._base_url}{self.PATH}")

    def fill_first_name(self, value: str) -> None:
        self.first_name_input.fill(value)

    def expect_first_name_value(self, expected: str) -> None:
        expect(self.first_name_input).to_have_value(expected)

    def fill_last_name(self, value: str) -> None:
        self.last_name_input.fill(value)

    def expect_last_name_value(self, expected: str) -> None:
        expect(self.last_name_input).to_have_value(expected)

    def invalid_name_value(self, disallowed: str) -> None:
        expect(self.first_name_input).not_to_have_value(disallowed)
        expect(self.last_name_input).not_to_have_value(disallowed)

    def fill_phone_number(self, value: str) -> None:
        self.phone_number_input.fill(value)

    def expect_phone_number_value(self, expected: str) -> None:
        expect(self.phone_number_input).to_have_value(expected)

    def invalid_phone_number_value(self, disallowed: str) -> None:
        expect(self.phone_number_input).not_to_have_value(disallowed)

    def select_country(self, country_value: str) -> None:
        self.country_dropdown.select_option(country_value)

    def expect_country_selected(self, expected_value: str) -> None:
        expect(self.country_dropdown).to_have_value(expected_value)

    def expect_country_dropdown_visible(self) -> None:
        expect(self.country_dropdown).to_be_visible()

    def fill_email(self, value: str) -> None:
        self.email_input.fill(value)    

    def expect_email_value(self, expected: str) -> None:
        expect(self.email_input).to_have_value(expected)

    def invalid_email_value(self, disallowed: str) -> None:
        expect(self.email_input).not_to_have_value(disallowed)
    
    def fill_password(self, value: str) -> None:
        self.password_input.fill(value)  

    def expect_password_value(self, expected: str) -> None:
        expect(self.password_input).to_have_value(expected)

    def invalid_password_value(self, disallowed: str) -> None:
        expect(self.password_input).not_to_have_value(disallowed)   
    
    def click_terms_and_conditions_checkbox(self) -> None:
        self.terms_and_conditions_checkbox.check()

    def expect_terms_and_conditions_checkbox_enabled(self) -> None:
        expect(self.terms_and_conditions_checkbox).to_be_enabled() 

    def submit_form(self) -> None:
        self.submit_button.click() 

    def expect_success_message_first_name(self, expected: str) -> None:
        expect(self.success_message_first_name).to_have_text(f"First Name: {expected}")

    def expect_success_message_last_name(self, expected: str) -> None:
        expect(self.success_message_last_name).to_have_text(f"Last Name: {expected}")

    def expect_success_message_phone_number(self, expected: str) -> None:
        expect(self.success_message_phone_number).to_have_text(f"Phone Number: {expected}")

    def expect_success_message_country(self, expected: str) -> None:
        expect(self.success_message_country).to_have_text(f"Country: {expected}")

    def expect_success_message_email(self, expected: str) -> None:
        expect(self.success_message_email).to_have_text(f"Email: {expected}")
    
    def expect_success_message(self, expected: str) -> None:
        expect(self.success_message_password).to_have_text(expected)