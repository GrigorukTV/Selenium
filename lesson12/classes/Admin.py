import time
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By


class Admin(BasePage):

    loginSelector = '#input-username'
    passwordSelector = '#input-password'
    buttonSelector = 'button[type="submit"]'

    def __init__(self, wd):
        self.wd = wd

    def get_heading(self):
        self.authorize('user', 'bitnami')
        self.click_element((By.CSS_SELECTOR, ".tile-primary:first-child .tile-footer a"))
        return self.wd.find_element_by_css_selector('h1').get_attribute('innerHTML').find('Orders')

    def settings(self):
        self.authorize('user', 'bitnami')
        self.click_element((By.CSS_SELECTOR, "#menu-system a"))
        self.click_element((By.CSS_SELECTOR, "#collapse7 > li:first-child a"))
        index = -1
        table = self.wd.find_element_by_css_selector('.table')
        if table is not None:
            cl_table = table.get_attribute('class')
            index = cl_table.find('table table-bordered table-hover')
        return index

    def product_table(self):
        self.authorize('user', 'bitnami')
        self.click_element((By.CSS_SELECTOR, "#menu-system a"))
        self.click_element((By.CSS_SELECTOR, "#menu-catalog a"))
        self.click_element((By.CSS_SELECTOR,'#collapse1 > li:nth-child(2) a'))

        index = -1
        table = self.wd.find_element_by_css_selector('.table')
        if table is not None:
            cl_table = table.get_attribute('class')
            index = cl_table.find('table-bordered table-hover')
        return index

    def admin_authorization(self):
        self.authorize('user', 'bitnami')
        logout = self.wd.find_element_by_css_selector('.navbar-right > li:last-child span')
        user_login = logout.get_attribute('innerHTML')
        index = user_login.find('Logout')
        return index

    def admin_logout(self):
        self.authorize('user', 'bitnami')
        self.click_element((By.CSS_SELECTOR, ".navbar-right > li:last-child a"))
        url = self.wd.current_url
        return url.find('?route=common/login')