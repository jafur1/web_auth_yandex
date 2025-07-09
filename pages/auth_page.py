from playwright.sync_api import Page

class AuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = '[data-testid="login-email-input"]'
        self.password_input = '[data-testid="login-password-input"]'
        self.submit_button = '[data-testid="login-submit-button"]'
        self.back_button = '[data-testid="login-back-button"]'
        self.register_button = '[data-testid="login-register-button"]'
        self.logout_button = '[data-testid="user-logout-button"]'
        self.main_login_button = '[data-testid="main-login-button"]'
        self.register_back_button = '[data-testid="register-back-button"]'
        self.edit_profile_button = '[data-testid="user-edit-profile-button"]'
        self.edit_name_input = '[data-testid="edit-name-input"]'
        self.edit_save_button = '[data-testid="edit-save-button"]'
        self.edit_cancel_button = '[data-testid="edit-cancel-button"]'
        self.edit_profile_text = 'div.css-146c3p1.r-vw2c0b.r-1yflyrw.r-q4m81j.r-1ui5ee8'
        self.profile_name_div = 'div.css-146c3p1.r-vw2c0b.r-15zivkp.r-evnaw'

    def goto_login(self):
        self.page.goto("https://yavshok.ru/login")
        self.page.wait_for_selector(self.email_input, timeout=5000)

    def goto_main(self):
        self.page.goto("https://yavshok.ru")
        self.page.wait_for_selector(self.main_login_button, timeout=5000)

    def fill_email(self, email: str):
        self.page.fill(self.email_input, email)

    def fill_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_submit(self):
        self.page.click(self.submit_button)

    def click_back(self):
        self.page.click(self.back_button)

    def click_register(self):
        self.page.click(self.register_button)

    def click_logout(self):
        self.page.wait_for_selector(self.logout_button, timeout=5000)
        self.page.click(self.logout_button)

    def click_main_login(self):
        self.page.click(self.main_login_button)

    def click_register_back(self):
        self.page.click(self.register_back_button)

    def login(self, email: str, password: str):
        self.fill_email(email)
        self.fill_password(password)
        self.click_submit()

    def is_logout_visible(self):
        return self.page.locator(self.logout_button).is_visible()

    def is_email_visible(self):
        return self.page.locator(self.email_input).is_visible()

    def is_main_login_visible(self):
        return self.page.locator(self.main_login_button).is_visible()

    def is_back_button_visible(self):
        return self.page.locator(self.back_button).is_visible()

    def wait_for_success_message(self, message: str):
        self.page.wait_for_selector(f'text={message}', timeout=5000)

    def wait_for_error_message(self, message: str):
        self.page.wait_for_selector(f'text={message}', timeout=5000)

    def is_message_visible(self, message: str):
        return self.page.locator(f'text={message}').is_visible()

    def is_gif_visible(self):
        return self.page.locator('img[src*="happyCat"]').is_visible()

    def get_message_color(self, message: str):
        element = self.page.locator(f'text={message}')
        return element.evaluate("el => getComputedStyle(el).color")

    