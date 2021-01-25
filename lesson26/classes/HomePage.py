from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#logo a")
    PRODUCT_LAYOUT_CHILD2 = (By.CSS_SELECTOR, ".product-layout:nth-child(2) h4 > a")
    SEARCH_INPUT_GROUP = (By.CSS_SELECTOR, "#search > .input-group-btn")
    MENU_COLLAPSE = (By.CSS_SELECTOR, "#menu > .collapse > .nav > li:nth-child(6) > a")
    COMPARE_TOTAL = (By.CSS_SELECTOR, "#compare-total")
    TOP_LINKS_CHILD = (By.CSS_SELECTOR, "#top-links > .list-inline > li:nth-child(5) > a")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    FOOTER_COL_SM = (By.CSS_SELECTOR, "footer .col-sm-3:first-child li:first-child a")
    CONTENT = (By.CSS_SELECTOR, "#content > h1")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, '.product-layout')
    FORM_CONTROL = (By.CSS_SELECTOR,'#search > .form-control')
    SEARCH_INPUT = (By.CSS_SELECTOR,'#search input')
    TOP_LINKS = (By.CSS_SELECTOR, "#top-links")
    FOOTER_LINKS_CHILD = (By.CSS_SELECTOR, "footer .col-sm-3:nth-child(2) > .list-unstyled > li:first-child a")
    log_path = "logs/HomePage.log"

    def get_title(self):
        title = self.wd.title
        return title

    def search_phone(self):
        topLinks = self.find_element(self.TOP_LINKS)
        listInline = topLinks.find_elements_by_class_name('list-inline')
        li = listInline[0].find_elements_by_tag_name('li')
        span = li[0].find_element_by_tag_name('span')
        return span.get_attribute('innerHTML')

    def get_length_product_layouts(self):
        return len(self.find_elements(self.PRODUCT_LAYOUT))

    def get_clicked_url(self):
        self.click_element(self.LOGO)
        url = self.wd.current_url
        return url

    def get_url_search(self):
        self.send_keys(self.FORM_CONTROL,'iphone')
        self.click_element(self.SEARCH_INPUT_GROUP)
        return self.url_to_be("http://192.168.0.14/index.php?route=product/search&search=iphone")

    def get_url_search_iphone(self):
        self.click_element(self.PRODUCT_LAYOUT_CHILD2)
        return self.url_to_be("http://192.168.0.14/iphone")

    def get_url_product_comparison(self):
        self.click_element(self.MENU_COLLAPSE)
        self.click_element(self.COMPARE_TOTAL)
        header = self.find_element(self.CONTENT)
        return header.get_attribute('innerHTML')

    def get_contact_us(self):
        self.click_element(self.FOOTER_LINKS_CHILD)
        return self.url_to_be("http://192.168.0.14/index.php?route=information/contact")

    def get_search(self):
        self.send_keys(self.SEARCH_INPUT, 'iphone')
        self.click_element(self.SEARCH_BUTTON)
        return self.url_to_be("http://192.168.0.14/index.php?route=product/search&search=iphone")

    def get_shopping_cart(self):
        self.click_element(self.TOP_LINKS_CHILD)
        el = self.find_element(self.CONTENT)
        return el.get_attribute('innerHTML')

    def get_footer_link(self):
        self.click_element(self.FOOTER_COL_SM)
        return self.url_to_be("http://192.168.0.14/about_us")






