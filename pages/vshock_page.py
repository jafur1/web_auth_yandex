from playwright.sync_api import Page

class VShockPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = '[data-testid="main-email-input"]'
        self.check_button = '[data-testid="main-check-button"]'

    def goto_main(self):
        self.page.goto("https://yavshok.ru")
        self.page.wait_for_selector(self.email_input, timeout=5000)

    def fill_email(self, email: str):
        self.page.fill(self.email_input, email)

    def click_check(self):
        self.page.click(self.check_button)

    def check_email_status(self, email: str):
        self.fill_email(email)
        self.click_check()

    def is_button_aria_disabled(self):
        button = self.page.locator(self.check_button)
        return button.get_attribute("aria-disabled") == "true"

    def wait_for_success_message(self, message: str):
        self.page.wait_for_selector(f'text={message}', timeout=5000)

    def wait_for_fail_message(self, message: str):
        self.page.wait_for_selector(f'text={message}', timeout=5000)

    def is_message_visible(self, message: str):
        return self.page.locator(f'text={message}').is_visible()

    def is_gif_visible(self):
        return self.page.locator('img[src*="happyCat"]').is_visible()

    def get_message_color(self, message: str):
        element = self.page.locator(f'text={message}')
        return element.evaluate("el => getComputedStyle(el).color") 