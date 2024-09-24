import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru-ru, fr, es")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language == "en":
        print("\nstart firefox browser in EN for test..")
        fp = FirefoxOptions()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=fp)
    elif user_language == "ru-ru":
        print("\nstart firefox browser in RU for test..")
        profile = FirefoxOptions()
        profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=profile)
    elif user_language == "fr":
        print("\nstart firefox browser in FR for test..")
        fp = FirefoxOptions()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=fp)
    elif user_language == "es":
        print("\nstart firefox browser in ES for test..")
        fp = FirefoxOptions()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=fp)
    else:
        raise pytest.UsageError("--language should be")
    yield browser
    print("\nquit browser..")
    browser.quit()