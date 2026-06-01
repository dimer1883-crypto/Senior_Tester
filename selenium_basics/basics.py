from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Запуск (Selenium Manager сам найдёт geckodriver)
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://demoqa.com/')

# Ожидание и клик
wait = WebDriverWait(browser, 10)
from_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']")))

browser.execute_script("arguments[0].click();", from_element)
time.sleep(5)
browser.quit()