import pytest
from pages.auth_page import AuthPage
from pages.vshock_page import VShockPage

TEST_TIMEOUT = 5000
BASE_URL = "https://yavshok.ru"

@pytest.fixture
def auth_page(page):
    "Фикстура для работы со страницей авторизации"
    return AuthPage(page)

@pytest.fixture
def vshock_page(page):
    "Фикстура для работы с главной страницей VShock"
    return VShockPage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    "Глобальные настройки браузера для всех тестов"
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
