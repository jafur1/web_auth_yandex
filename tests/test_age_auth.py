import pytest
from data.auth_age_data import EMAIL_MIN, WRONG_PASSWORD_MIN, EMAIL_MEDIUM, WRONG_PASSWORD_MEDIUM, EMAIL_MAX, WRONG_PASSWORD_MAX

def test_auth_min_age_status(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL_MIN, WRONG_PASSWORD_MIN)
    auth_page.wait_for_success_message("Ты молоденький котик")
    assert auth_page.is_message_visible("Ты молоденький котик"), "Статус 'Ты молоденький котик' не найден"

def test_auth_medium_age_status(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL_MEDIUM, WRONG_PASSWORD_MEDIUM)
    auth_page.wait_for_success_message("Ты старый котик")
    assert auth_page.is_message_visible("Ты старый котик"), "Статус 'Ты старый котик' не найден (medium)"

def test_auth_max_age_status(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL_MAX, WRONG_PASSWORD_MAX)
    auth_page.wait_for_success_message("Ты старый котик")
    assert auth_page.is_message_visible("Ты старый котик"), "Статус 'Ты старый котик' не найден (max)"
