from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    # Аргументы специально для GitHub Actions (Linux)
    options.add_argument('--headless=new')  # Запуск без окна
    options.add_argument('--no-sandbox')  # Обязательно для CI (Ubuntu)
    options.add_argument('--disable-dev-shm-usage')  # Чтобы не падало по памяти
    options.add_argument('--window-size=1920,1080')  # Полноэкранный режим

    browser = webdriver.Chrome(options=options)  # Инициализируем Chrome
    browser.maximize_window()
    browser.implicitly_wait(5)  # Чуть увеличил ожидание для стабильности
    yield browser
    browser.quit()