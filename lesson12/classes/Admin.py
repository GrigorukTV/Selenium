import logging
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By


class Admin(BasePage):
    TILE_PRIMARY = (By.CSS_SELECTOR, ".tile-primary:first-child .tile-footer a")
    H1 = (By.CSS_SELECTOR,'h1')
    MENU_SYSTEM = (By.CSS_SELECTOR, "#menu-system a")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog a")
    COLLAPSE1 = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) a')
    COLLAPSE7 = (By.CSS_SELECTOR, "#collapse7 > li:first-child a")
    TABLE = (By.CSS_SELECTOR, ".table")
    NAVBAR = (By.CSS_SELECTOR, ".navbar-right > li:last-child span")
    NAVBAR_CHILD_A = (By.CSS_SELECTOR, ".navbar-right > li:last-child a")
    loginSelector = '#input-username'
    passwordSelector = '#input-password'
    buttonSelector = 'button[type="submit"]'
    log_path = "logs/Admin.log"


    def get_heading(self):
        self.authorize('user', 'bitnami')
        self.click_element(self.TILE_PRIMARY)
        return self.find_element(self.H1).get_attribute('innerHTML').find('Orders')

    def settings(self):
        self.authorize('user', 'bitnami')
        self.click_element(self.MENU_SYSTEM)
        self.click_element(self.COLLAPSE7)
        index = -1
        table = self.find_element(self.TABLE)
        if table is not None:
            cl_table = table.get_attribute('class')
            index = cl_table.find('table table-bordered table-hover')
        return index

    def product_table(self):
        self.authorize('user', 'bitnami')
        self.click_element(self.MENU_SYSTEM)
        self.click_element(self.MENU_CATALOG)
        self.click_element(self.COLLAPSE1)

        index = -1
        table = self.find_element(self.TABLE)
        if table is not None:
            cl_table = table.get_attribute('class')
            index = cl_table.find('table-bordered table-hover')
        return index

    def admin_authorization(self):
        self.authorize('user', 'bitnami')
        logout = self.find_element(self.NAVBAR)
        user_login = logout.get_attribute('innerHTML')
        index = user_login.find('Logout')
        return index

    def admin_logout(self):
        self.authorize('user', 'bitnami')
        self.click_element(self.NAVBAR_CHILD_A)
        url = self.wd.current_url
        return url.find('?route=common/login')