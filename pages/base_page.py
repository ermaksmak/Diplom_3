import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.personal_account_locator import button_personal_account
from url import URL
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)
        self.wait = WebDriverWait(self.browser, 20)

    @allure.step('Общий метод для получения атрибута элемента')
    def get_attribute_of_element(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    @allure.step('Явное ожидание. Пока элемент не будет кликабелен')
    def wait(self, locator):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        return self.browser.find_element(*locator)

    @allure.step('Ждет загрузки страницы с указанным URL.')
    def wait_for_page_load(self, url):
        wait_o = WebDriverWait(self.browser, 10)
        wait_o.until(EC.url_to_be(url))

    @allure.step('Поиск элемента')
    def find_element(self, *args):
        return self.browser.find_element(*args)

    @allure.step('Общий метод для поиска элемента')
    def find(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, *args):
        return self.browser.find_elements(*args)

    @allure.step('Общий метод для клика по элементу')
    def click_element(self, locator):
        element = self.find(locator)
        element.click()

    @allure.step('Общий метод для ввода данных')
    def send_keys(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)

    @allure.step('Открывает главную страницу')
    def open(self, url=None):
        if url is not None:
            self.browser.get(url)
        else:
            self.browser.get(URL)

    @allure.step('Возвращаем текущую страницу')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Общий метод для получения текста элемента')
    def get_text_of_element(self, locator):
        element = self.find(locator)
        return element.text

    @allure.step('Нажимает на кнопку "Личный кабинет')
    def click_personal_account(self):
        self.click_element(button_personal_account)