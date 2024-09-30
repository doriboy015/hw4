from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import MainPageLocators

class BasketPage(BasePage):
    def go_to_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_CLASS), "Product is presented"

    def should_be_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_OUTER), "Text is not presented"
