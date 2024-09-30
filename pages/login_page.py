from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        button = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        button.click()
        register_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        register_input.send_keys(email)
        register_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS1)
        register_input.send_keys(password)
        register_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS2)
        register_input.send_keys(password)
        register_input = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_input.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS), "Don't view message"

