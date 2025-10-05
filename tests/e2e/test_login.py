from __future__ import annotations

import pytest
from playwright.sync_api import Page
from tests.pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.smoke
class TestLogin:
    
    def test_tc_auth_001_login_with_valid_credentials(
        self,
        page: Page,
        base_url: str,
        default_credentials: dict[str, str],
    ) -> None:
        login_page = LoginPage(page, base_url)
        login_page.visit()
        login_page.login(
            email=default_credentials["email"],
            password=default_credentials["password"],
        )
        login_page.expect_authenticated_nav()