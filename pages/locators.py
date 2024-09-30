from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.NAME, 'registration-email')
    REGISTER_FORM_PASS1 = (By.NAME, 'registration-password1')
    REGISTER_FORM_PASS2 = (By.NAME, 'registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')
    REGISTER_SUCCESS = (By.XPATH, '//*[@id="messages"]/div/div')

class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_NEW = (By.CSS_SELECTOR, '.alertinner > strong')
    PRODUCT_NAME_OLD = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    NEW_SIZE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    OLD_SIZE = (By.CLASS_NAME, 'basket-mini.pull-right.hidden-xs')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner')

class BasketPageLocators():
    PRODUCT_CLASS = (By.CLASS_NAME, 'basket-items')
    TEXT_OUTER = (By.XPATH, '//div[@id="content_inner"][1]')

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")