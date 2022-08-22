from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
import time


def calc():
    return str(math.log(abs(12 * math.sin(int(x)))))               # функция расчитает значение, для поля ввода


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)


WebDriverWait(browser, 12).until(  # Selenium ждёт 12 сек., пока кнопка не станет кликабельной,и второе условие
    ec.text_to_be_present_in_element((By.CSS_SELECTOR, "#price", ), '100'))  # ждём пока цена не упадёт до 100$

browser.find_element(By.CSS_SELECTOR, "button#book").click()                 # кликаем кнопку

x_element = browser.find_element(By.ID, "input_value")          # find the value, of the selected item
x = x_element.text                                              # get value (.text) between tags
y = calc()                                                      # variable 'y', store a calculated number from the def

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)   # find the input field, and enter 'y' value

browser.find_element(By.CSS_SELECTOR, "#solve").click()         # click button

time.sleep(15)
browser.quit()









