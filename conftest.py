import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # парсер выбора браузера при запуске из терминала "--browser_name=<браузер>"
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # парсер выбора языка при запуске из терминала "--languege=<язык>"
    parser.addoption('--language', action='store',
                     default='ru', help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")  # запрос, get и use браузера из команды запуска теста
    user_language = request.config.getoption("language")     # запрос, get и use языка из команды запуска теста
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # назначаем язык браузера, используя Класс Option и метод add.experemental_option
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
