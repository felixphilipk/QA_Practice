from __future__ import annotations
import pytest

DEFAULT_BASE_URL = "https://qa-practice.netlify.app"
DEFAULT_CREDENTIALS = {
    "email": "admin@admin.com",
    "password": "admin123",
}

@pytest.fixture(scope="session")
def base_url() -> str:
    return DEFAULT_BASE_URL

@pytest.fixture()
def default_credentials() -> dict[str, str]:
    return DEFAULT_CREDENTIALS.copy()
