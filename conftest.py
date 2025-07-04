import pytest
from playwright.sync_api import sync_playwright
from auth_lib.auth import load_cookies

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Можно добавить глобальные настройки контекста
    return browser_context_args

@pytest.fixture(scope="function")
def page(browser_context_args, request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**browser_context_args)
        # Загружаем куки, если не тест логина
        if "login" not in request.node.name:
            load_cookies(context)
        page = context.new_page()
        yield page
        context.close()
        browser.close() 