from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_products()
    page.should_be_text()

