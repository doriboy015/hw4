from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import math
import time
import pytest

class ProductPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.product_size_new = None
        self.product_name_new = None
        self.fin_size_old = None
        self.product_name_old = None

    def test_add_to_basket(self):
        self.go_to_basket_alert()
        self.solve_quiz_and_get_code()
        self.test_old_book()
        self.test_new_book()
        self.test_new_size()
        self.test_old_size()
    def go_to_basket_alert(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        basket_button.click()
        time.sleep(1)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(6)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            # print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        # time.sleep(20)

    def test_old_book(self):
        try:
            assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_OLD), "Not found old book"
            self.product_name_old = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_OLD).text
            # print(f"Your old book: {product_name_old}")
        except NoSuchElementException:
            print("No old book")

    def test_old_size(self):
        try:
            assert self.is_element_present(*ProductPageLocators.OLD_SIZE), "Not found old size"
            product_size_old = self.browser.find_element(*ProductPageLocators.OLD_SIZE).text
            size_old = product_size_old.split(" ")
            self.fin_size_old = size_old[2][:6]
            # print(f"Your old size: {fin_size_old}")
        except NoSuchElementException:
            print("No old size")

    def test_new_book(self):
        try:
            assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_NEW), "Not found new book"
            self.product_name_new = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_NEW).text
            # print(f"Your new book: {product_name_new}")
        except NoSuchElementException:
            print("No new book")

    def test_new_size(self):
        try:
            assert self.is_element_present(*ProductPageLocators.NEW_SIZE), "Not found new size"
            self.product_size_new = self.browser.find_element(*ProductPageLocators.NEW_SIZE).text
            # print(f"Your new size: {product_size_new}")
        except NoSuchElementException:
            print("No new size")

    def test_size_and_name(self):
        assert self.product_name_old == self.product_name_new, 'Названия книг не совпадают'
        assert self.product_size_new == self.fin_size_old, 'Стоимость не совпадает'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not"


