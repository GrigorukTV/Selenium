import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, remote):
        self.wd = remote
        self.logger = logging.getLogger(type(self).__name__)
        f = logging.FileHandler(filename=self.log_path)
        f.setLevel(logging.INFO)
        self.logger.addHandler(f)


    def authorize(self, login='', password=''):
        login_field = self.wd.find_element_by_css_selector(self.loginSelector)
        login_field.send_keys(login)
        password_field = self.wd.find_element_by_css_selector(self.passwordSelector)
        password_field.send_keys(password)
        login_bt = self.wd.find_element_by_css_selector(self.buttonSelector)
        self.logger.info("User {},{} is authorized".format(login, password))
        login_bt.click()

    @allure.step("Получить элемент {locator}")
    def find_element(self, locator, time=2):
        self.logger.info("Получить элемент {}".format(locator))
        return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator))

    @allure.step("Получить элементы {locator}")
    def find_elements(self, locator, time=2):
        self.logger.info("Получить элементы {}".format(locator))
        return WebDriverWait(self.wd, time).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Выполняю клик по элементу {locator}")
    def click_element(self, locator, time=3):
        self.logger.info("Clicking element {}".format(locator))
        try:
            WebDriverWait(self.wd, time).until(EC.element_to_be_clickable(locator)).click()
            return self
        except TimeoutException:
            allure.attach(
                body=self.wd.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def send_keys(self, locator, text, time=5):
        self.logger.info("Text input: {}".format(text))
        allure.attach(
            body=self.wd.get_screenshot_as_png(),
            name="screenshot_image",
            attachment_type=allure.attachment_type.PNG)
        return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator)).send_keys(text)

    @allure.step("Открываю url {locator}")
    def url_to_be(self, locator, time=5):
        return WebDriverWait(self.wd, time).until(EC.url_to_be(locator))

    @allure.step("Проверяю url {locator}")
    def url_changes(self, locator, time=1):
        return WebDriverWait(self.wd, time).until(EC.url_changes(locator))

    @allure.step("Получаю количество элементов")
    def return_len(self, locator):
        elements = self.wd.find_elements_by_css_selector(locator)
        return len(elements)

    def text_present(self, locator, time=5):
        return WebDriverWait(self.wd, time).until(EC.text_to_be_present_in_element(locator))

    def element_located(self, locator, time=5):
        return WebDriverWait(self.wd, time).until(EC.visibility_of_element_located(locator))

    def elements_located(self, locator, time=5):
        return WebDriverWait(self.wd, time).until(EC.visibility_of_any_elements_located(locator))
