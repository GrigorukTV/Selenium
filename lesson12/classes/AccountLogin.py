import logging
from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By


class AccountLogin(BasePage):

    MESSAGE = (By.CLASS_NAME, "alert")
    ACCOUNT = (By.CSS_SELECTOR, "#content > h2")
    WELL_CHILD = (By.CSS_SELECTOR, ".well:first-child a")
    INPUT = (By.CSS_SELECTOR, "input[type='submit']")
    FORM_GROUP = (By.CSS_SELECTOR, ".form-group a")
    log_path = "logs/AccountLogin.log"

    def get_clicked_url(self):
        self.click_element(self.WELL_CHILD)
        return self.url_to_be("http://192.168.0.12/index.php?route=account/register")

    def get_message_danger(self):
        self.click_element(self.INPUT)
        index = -1
        message = self.find_element(self.MESSAGE)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-danger')
        return index

    def get_url_forgotten(self):
        self.click_element(self.FORM_GROUP)
        return self.url_to_be("http://192.168.0.12/index.php?route=account/forgotten")

    def get_message_not_login(self):
        self.authorize('12@tests.ru','123')
        message = self.find_element(self.MESSAGE)
        user_none = message.get_attribute('innerHTML')
        index = user_none.find('E-Mail Address and/or Password')
        return index

    def get_heading_account(self):
        self.autorize('tests@tests.ru', '1234')
        account = self.find_elements(self.ACCOUNT)
        my_account = account[0].get_attribute('innerHTML')
        index = my_account.find('My Account')
        return index



