import time
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By


class AccountLogin(BasePage):

    message = (By.CLASS_NAME, "alert")
    account = (By.CSS_SELECTOR, "#content > h2")

    loginSelector = '#input-email'
    passwordSelector = '#input-password'
    buttonSelector = 'input[type="submit"]'


    def __init__(self, wd):
        self.wd = wd

    def get_clicked_url(self):
        self.click_element((By.CSS_SELECTOR, ".well:first-child a"))
        return self.url_to_be("http://localhost/index.php?route=account/register")

    def get_message_danger(self):
        self.click_element((By.CSS_SELECTOR, "input[type='submit']"))
        index = -1
        message = self.find_element(locator=self.message)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-danger')
        return index

    def get_url_forgotten(self):
        self.click_element((By.CSS_SELECTOR, ".form-group a"))
        return self.url_to_be("http://localhost/index.php?route=account/forgotten")

    def get_message_not_login(self):
        self.authorize('12@tests.ru','123')
        message = self.find_element(locator=self.message)
        user_none = message.get_attribute('innerHTML')
        index = user_none.find('E-Mail Address and/or Password')
        return index

    def get_heading_account(self):
        self.autorize('tests@tests.ru', '1234')
        account = self.find_elements(self.account)
        my_account = account[0].get_attribute('innerHTML')
        index = my_account.find('My Account')
        return index



