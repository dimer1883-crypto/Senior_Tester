from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(2)
    yield browser
    browser.quit()