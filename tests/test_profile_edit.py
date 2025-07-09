import pytest
from playwright.sync_api import sync_playwright
from pages.auth_page import AuthPage
from data.auth_age_data import EMAIL_MIN, WRONG_PASSWORD_MIN

PROFILE_EDIT_URL = "https://yavshok.ru/edit?__EXPO_ROUTER_key=undefined-ljv57MTE6Ja4SADFxd6Z9"
MAIN_URL = "https://yavshok.ru/"

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def auth_page(page):
    return AuthPage(page)

def test_edit_profile_button_and_text(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL_MIN, WRONG_PASSWORD_MIN)
    auth_page.page.wait_for_selector(auth_page.logout_button, timeout=5000)
    auth_page.page.wait_for_selector('[data-testid="user-edit-profile-button"]', timeout=5000)
    auth_page.page.click('[data-testid="user-edit-profile-button"]')
    el = auth_page.page.wait_for_selector('div.css-146c3p1.r-vw2c0b.r-1yflyrw.r-q4m81j.r-1ui5ee8', timeout=5000)
    assert el.inner_text() == "Edit Profile"

def test_edit_and_save_name(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL_MIN, WRONG_PASSWORD_MIN)
    auth_page.page.wait_for_selector(auth_page.logout_button, timeout=5000)
    auth_page.page.wait_for_selector('[data-testid="user-edit-profile-button"]', timeout=5000)
    auth_page.page.click('[data-testid="user-edit-profile-button"]')
    auth_page.page.fill('[data-testid="edit-name-input"]', 'neko1')
    auth_page.page.click('[data-testid="edit-save-button"]')
    auth_page.page.click('[data-testid="edit-cancel-button"]')
    auth_page.page.goto(MAIN_URL)
    el = auth_page.page.wait_for_selector('div.css-146c3p1.r-vw2c0b.r-15zivkp.r-evnaw', timeout=5000)
    assert el.inner_text() == "neko1"

def test_edit_save_button_visible(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL_MIN, WRONG_PASSWORD_MIN)
    auth_page.page.wait_for_selector(auth_page.logout_button, timeout=5000)
    auth_page.page.wait_for_selector('[data-testid="user-edit-profile-button"]', timeout=5000)
    auth_page.page.click('[data-testid="user-edit-profile-button"]')
    # Проверяем наличие кнопки сохранения
    el = auth_page.page.wait_for_selector('[data-testid="edit-save-button"]', timeout=5000)
    assert el.is_visible()