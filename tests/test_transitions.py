import pytest
from data.auth_data import EMAIL, PASSWORD

def test_transitions_between_eavesdropping_and_authorization(auth_page):
    auth_page.goto_main()
    auth_page.click_main_login()
    auth_page.click_back()
    assert auth_page.is_main_login_visible(), "Страница входа не найдена"

def test_transitions_between_authorization_and_registration(auth_page):
    auth_page.goto_login()
    auth_page.click_register()
    auth_page.click_register_back()
    assert auth_page.is_back_button_visible(), "Страница входа не найдена"



