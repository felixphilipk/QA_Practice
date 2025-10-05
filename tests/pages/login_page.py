from __future__ import annotations
from playwright.sync_api import Locator, Page, expect


class LoginPage:

    PATH = "/auth_ecommerce.html"

    def __init__(self, page: Page, base_url: str) -> None:
        self._page = page
        self._base_url = base_url.rstrip("/")

    @property
    def page(self) -> Page:
        return self._page

    @property
    def email_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="Email")

    @property
    def password_input(self) -> Locator:
        return self._page.get_by_role("textbox", name="Password")

    @property
    def submit_button(self) -> Locator:
        return self._page.get_by_role("button", name="Submit")

    def visit(self) -> None:
        self._page.goto(f"{self._base_url}{self.PATH}")

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_authenticated_nav(self) -> None:
        expect(self._page.get_by_role("link", name="Home")).to_be_visible()
        expect(self._page.get_by_role("link", name="Contact")).to_be_visible()
        expect(self._page.get_by_role("heading", name="SHOPPING CART")).to_be_visible()
