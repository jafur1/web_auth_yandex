import pytest
from playwright.sync_api import expect

LOGIN_URL = "https://yavshok.ru/login"


def test_login_page_title(page):
    page.goto(LOGIN_URL)
    assert "Вход" in page.title()

def test_login_form_visible(page):
    page.goto(LOGIN_URL)
    assert page.is_visible("form")

def test_login_button_disabled_on_empty(page):
    page.goto(LOGIN_URL)
    assert page.is_disabled("button[type='submit']") 