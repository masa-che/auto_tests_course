from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_find_button_add_to_basket(browser):
    browser.get(link)
    # в items положим длину (len) найденных элементов (find_elements) по селектору
    # в assert сравним полученную длину, если items не больше нуля выпадет assert(условие задачи)
    items = len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"))
    assert items > 0, "Кнопка добавления товара в корзину отсутствует"



