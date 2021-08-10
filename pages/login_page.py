from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_1)
        password_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_2)
        submit_btn = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        email_input.send_keys(email)
        password_1.send_keys(password)
        password_2.send_keys(password)
        submit_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, "Login url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
