import logging
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By


class AccountLoginAdm(BasePage):


    loginSelector = '#input-username'
    passwordSelector = '#input-password'
    buttonSelector = 'button[type="submit"]'
    MESSAGE_SELECTOR = (By.CSS_SELECTOR, ".alert")
    CLOSE = (By.CSS_SELECTOR, ".alert > .close")
    MES_DANGER_SELECTOR = 'alert-danger'
    log_path = "logs/AccountLoginAdm.log"

    def get_message_danger(self):
        self.authorize()
        index = -1
        message = self.find_element(self.MESSAGE_SELECTOR)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find(self.MES_DANGER_SELECTOR)
        return index

    def get_message_danger_not_pass(self):
        self.authorize(login='user')
        index = -1
        message = self.find_element(self.MESSAGE_SELECTOR)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find(self.MES_DANGER_SELECTOR)
        return index

    def get_message_danger_not_login(self):
        self.authorize(password='bitnami')
        index = -1
        message = self.find_element(self.MESSAGE_SELECTOR)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find(self.MES_DANGER_SELECTOR)
        return index

    def check_login_error_close(self):
        self.authorize(login='user')
        self.click_element(self.CLOSE)
        return self.return_len(".alert")

    def check_authorization_user(self):
        self.authorize('user', 'bitnami')
        return self.url_changes("http://192.168.0.12/admin/")