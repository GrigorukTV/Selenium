from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def authorize(self, login='', password=''):
        login_field = self.wd.find_element_by_css_selector(self.loginSelector)
        login_field.send_keys(login)
        password_field = self.wd.find_element_by_css_selector(self.passwordSelector)
        password_field.send_keys(password)
        login_bt = self.wd.find_element_by_css_selector(self.buttonSelector)
        login_bt.click()

    def find_element(self, locator, time=2):
        return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=2):
        return WebDriverWait(self.wd, time).until(EC.presence_of_all_elements_located(locator))


    def click_element(self,locator, time=10):
        WebDriverWait(self.wd, time).until(EC.element_to_be_clickable(locator)).click()

    def url_to_be(self,locator, time=10):
        return WebDriverWait(self.wd, time).until(EC.url_to_be(locator))

    def url_changes(self,locator, time=1):
        return WebDriverWait(self.wd, time).until(EC.url_changes(locator))

    def return_len(self, selector):
        elements = self.wd.find_elements_by_css_selector(selector)
        return len(elements)

