import time
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By

class AccountLoginAdm(BasePage):

    loginSelector = '#input-username'
    passwordSelector = '#input-password'
    buttonSelector = 'button[type="submit"]'
    messageSelector = (By.CSS_SELECTOR, ".alert")
    mesDangerSelector = 'alert-danger'

    def __init__(self, wd):
        self.wd = wd

    def get_message_danger(self):
        self.authorize()
        index = -1
        message = self.find_element(locator=self.messageSelector)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find(self.mesDangerSelector)
        return index

    def get_message_danger_not_pass(self):
        self.authorize(login='user')
        index = -1
        message = self.find_element(locator=self.messageSelector)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find(self.mesDangerSelector)
        return index

    def get_message_danger_not_login(self):
        self.authorize(password='bitnami')
        index = -1
        message = self.find_element(locator=self.messageSelector)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find(self.mesDangerSelector)
        return index

    def check_login_error_close(self):
        self.authorize(login='user')
        self.click_element((By.CSS_SELECTOR, ".alert > .close"))
        return self.return_len(".alert")

    def check_authorization_user(self):
        self.authorize('user', 'bitnami')
        return self.url_changes("http://localhost/admin/")