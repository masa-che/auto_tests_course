import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# комент -  для не стабильно работающей строки 44 с вызовом expected condition и WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait


# фикстура для открывания браузера , для каждого тест-кейса (def test_link)
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)        # для ожидания прогрузки страницы с url
    yield browser
    print("\nquit browser..")
    time.sleep(5)                      # для визуальной проверки прохождения тест-кейса
    browser.quit()


# фикстура с параметрами которые будут передавать в url функции def test_link
# - аргументы массива [https://stepik.org/lesson/236895/step/1 и т.д по очереди]
@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestUFO:                              # выжно начинать имя класса с Test (для pytest)
    def test_link(self, browser, links):    # функция открывает browser подставляя аргументы переменной links
        url = links
        browser.get(url)
        # ищем поле ввода ("ember-text-area"),
        # вставляем в поле результат вычисления функции (math.log(int(time.time) оборачивая результат str-ой
        browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(str(math.log(int(time.time()))))
        # ищем кнопку ("submit-submission") .кликаем её
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        # комент часть кода(работает не стабильно-  рабочий код переписан в строке 42)
        # WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
        # поиск текстового сообщения на странице .text , упаковываем в переменную find_correct_elm
        find_correct_elm = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        # сравнение найденного текста "smart-hints__hint" с текстом по заданию "Correct!"
        # f' строка вернёт значение {find_correct_elm} в переменной real , если assert False, т.е. не "Correct!"
        assert find_correct_elm == 'Correct!', f'Feedback is not "Correct!", real={find_correct_elm}'
