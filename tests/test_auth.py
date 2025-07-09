import pytest
from data.auth_data import EMAIL, WRONG_PASSWORD

def test_login_form_visible(auth_page):
    auth_page.goto_login()
    assert auth_page.is_email_visible(), "Поле Email не найдено"
    assert auth_page.page.locator(auth_page.password_input).is_visible(), "Поле Пароль не найдено"

def test_login_with_wrong_password(auth_page):
    auth_page.goto_login()
    auth_page.login(EMAIL, WRONG_PASSWORD)
    auth_page.wait_for_error_message("Неправильный логин или пароль")
    assert auth_page.is_message_visible("Неправильный логин или пароль"), "Сообщение о неправильном пароле не найдено"

def test_login_without_password(auth_page):
    auth_page.goto_login()
    auth_page.fill_email(EMAIL)
    auth_page.click_submit()
    auth_page.wait_for_error_message("Введите пароль")
    assert auth_page.is_message_visible("Введите пароль"), "Сообщение 'Введите пароль' не найдено"


