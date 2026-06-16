from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

users = ['user1','user2','user3']
passws = ['pass1', 'pass2', 'pass3']

# функция для перебора логинов и паролей так же в результате показывает для каждого теста какой логин и пароль использовался в конкретном тесте
def generate_pairs():
    pairs = []
    for user in users:
        for passw in passws:
            pairs.append(pytest.param((user, passw), id=f'{user}, {passw}'))
    return pairs


# Тут пробовали выбодить праметры для понимания какой пароль в каком тесте используется.
# @pytest.mark.parametrize(
#     'creds',
#     [
#         pytest.param(('user1', 'pass1'), id='user1, pass1'),
#         pytest.param(('user2', 'pass2'), id='user2, pass2'),
#         pytest.param(('user3', 'pass3'), id='user3, pass3'),
#     ]
# )

@pytest.mark.skip  # пропускать тест mark
@pytest.mark.parametrize('creds', generate_pairs())  # тут мы берем пары логинов и паролей где к каждому логину подбирается каждый пароль
def test_login(creds):
    login, passw = creds
    driver = webdriver.Chrome() # открытие браузера
    driver.get('https://www.okulik.by/accounts/login/?next=/kabinet/') # переход на UPL авторизации
    driver.implicitly_wait(2) # время ожидания
    driver.find_element(By.ID, 'id_username').send_keys(login) # логин и ввод логина
    driver.find_element(By.ID, 'id_password').send_keys(passw)  # password и ввод пароля
    driver.find_element(By.ID, 'submit-id-submit').click() # Кнопка входа и клик
    error_message = driver.find_element(By.CSS_SELECTOR, '.alert-danger li').text # сообщение об ошибке
    assert 'Неправильное имя пользователя или пароль' == error_message # ожидаемый результат

@pytest.fixture() # тут фикстура сразу для 2 страниц в зависимости какую вызовет функция
def page(request):
    driver = webdriver.Chrome()  # открытие браузера
    driver.implicitly_wait(2) # время ожидания
    param = request.param
    if param == 'video_stage':
        driver.get('https://okulik.by/item/video-stage/')
    elif param == '#prices':
        driver.get('https://www.okulik.by/#prices')
    return driver

@pytest.mark.parametrize('page', ['video_stage'], indirect=True)
def test_video_stage(page):
    video_stage = page.find_element(By.CSS_SELECTOR, 'h4.my-0.fw-normal')
    assert video_stage.text == 'Доступ к видеокурсу по автоматизации тестирования на Python - Рассрочка'

@pytest.mark.parametrize('page', ['#prices'], indirect=True)
def test_prices(page):
    title = page.find_element(By.XPATH, '//h1[text()="Цены"]')
    assert title.text == 'Цены'