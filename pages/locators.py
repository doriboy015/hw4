from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_NEW = (By.CSS_SELECTOR, '.alertinner > strong')
    PRODUCT_NAME_OLD = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    NEW_SIZE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    OLD_SIZE = (By.CLASS_NAME, 'basket-mini.pull-right.hidden-xs')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner')