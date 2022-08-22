from selenium import webdriver
from selenium.webdriver.common.by import By
# import os
import time
import math


def calc():
    return str(math.log(abs(12 * math.sin(int(x)))))                   # math function calculate, for enter field


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


browser.find_element(By.CSS_SELECTOR, "button.trollface").click()      # click to troll_button

new_window = browser.window_handles[1]                                 # get all arrow of tab (you need [1] )
browser.switch_to.window(new_window)                                   # switch to new window

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")      # find the value, of the selected item
x = x_element.text                                                     # get value (.text) between tags
y = calc()                                                             # variable 'y' store, calculated number from the def

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)          # find the input field, and enter 'y' value

browser.find_element(By.CSS_SELECTOR, "button.btn").click()            # click button 'Submit'


time.sleep(15)
browser.quit()







