import pytest

def test_vshock_button_aria_disabled_until_email(vshock_page):
    vshock_page.goto_main()
    assert vshock_page.is_button_aria_disabled(), "Кнопка должна иметь aria-disabled='true' при пустом email"
    vshock_page.fill_email('a')
    assert not vshock_page.is_button_aria_disabled(), "Кнопка не должна иметь aria-disabled='true' после ввода символа"

def test_vshock_success_email(vshock_page):
    vshock_page.goto_main()
    vshock_page.check_email_status('test@yandex.ru')
    vshock_page.wait_for_success_message("Ты уже в ШОКе")
    assert vshock_page.is_message_visible("Ты уже в ШОКе"), "Сообщение об успехе не найдено"
    assert vshock_page.is_gif_visible(), "Гифка happyCat не найдена"

def test_vshock_fail_email(vshock_page):
    vshock_page.goto_main()
    vshock_page.check_email_status('test@test.rrrrrre')
    vshock_page.wait_for_fail_message("Ты еще не в ШОКе")
    assert vshock_page.is_message_visible("Ты еще не в ШОКе"), "Сообщение о неуспехе не найдено"
    color = vshock_page.get_message_color("Ты еще не в ШОКе")
    assert color in ("rgb(255, 0, 0)", "#ff0000"), f"Ожидался красный цвет текста, а получен: {color}"
