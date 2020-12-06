import time
from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, wd):
        self.wd = wd

    def get_title(self):
        title = self.wd.title
        return title

    def search_phone(self):
        topLinks = self.wd.find_element_by_id('top-links')
        listInline = topLinks.find_elements_by_class_name('list-inline')
        li = listInline[0].find_elements_by_tag_name('li')
        span = li[0].find_element_by_tag_name('span')
        return span.get_attribute('innerHTML')

    def get_length_product_layouts(self):
        product_layouts = self.wd.find_elements_by_css_selector('.product-layout')
        return len(product_layouts)

    def get_clicked_url(self):
        self.click_element((By.CSS_SELECTOR, "#logo a"))
        url = self.wd.current_url
        return url

    def get_url_search(self):
        search = self.wd.find_element_by_css_selector('#search > .form-control')
        search.send_keys('iphone')
        self.click_element((By.CSS_SELECTOR, "#search > .input-group-btn"))
        return self.url_to_be("http://localhost/index.php?route=product/search&search=iphone")


    def get_url_search_iphone(self):
        self.click_element((By.CSS_SELECTOR, ".product-layout:nth-child(2) h4 > a"))
        return self.url_to_be("http://localhost/iphone")

    def get_url_product_comparison(self):
        self.click_element((By.CSS_SELECTOR, "#menu > .collapse > .nav > li:nth-child(6) > a"))
        self.click_element((By.CSS_SELECTOR, "#compare-total"))
        header = self.wd.find_element_by_css_selector('#content h1')
        return header.get_attribute('innerHTML')

    def get_contact_us(self):
        self.click_element((By.CSS_SELECTOR, "#top-links > .list-inline > li:first-child > a"))
        return self.url_to_be("http://localhost/index.php?route=information/contact")

    def get_search(self):
        search = self.wd.find_element_by_css_selector('#search > input')
        search.send_keys('iphone')
        self.click_element((By.CSS_SELECTOR, "#search button"))
        return self.url_to_be("http://localhost/index.php?route=product/search&search=iphone")

    def get_shopping_cart(self):
        self.click_element((By.CSS_SELECTOR, "#top-links > .list-inline > li:last-child > a"))
        el = self.find_element((By.CSS_SELECTOR, "#content > h1"))
        return el.get_attribute('innerHTML')

    def get_footer_link(self):
        self.click_element((By.CSS_SELECTOR, "footer .col-sm-3:first-child li:first-child a"))
        return self.url_to_be("http://localhost/about_us")






