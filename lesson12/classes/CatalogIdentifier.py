import time
from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CatalogId(BasePage):
    text = 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def __init__(self, wd):
        self.wd = wd

    def get_len_elements(self):
        count_elements = self.wd.find_elements_by_class_name('image-additional')
        return len(count_elements)

    def get_price(self):
        element = self.wd.find_element_by_css_selector('.list-unstyled h2')
        price = element.get_attribute('innerHTML')
        price = float(price.replace('$', ''))
        return price

    def get_number_product(self):
        # element_product = self.wd.find_element_by_css_selector('#button-cart')
        # element_product.click()
        self.click_element((By.CSS_SELECTOR, "#button-cart"))
        WebDriverWait(self.wd, 2).until(
            EC.text_to_be_present_in_element((By.ID, 'cart-total'), '0 item(s) - $0.00')
        )
        el = self.wd.find_element_by_css_selector('#cart-total')
        cart = el.get_attribute('innerHTML')
        index = cart.find('1 item')
        return index

    def get_url_gallery(self):
        element = self.wd.find_element_by_css_selector('.thumbnails .thumbnail')
        href = element.get_attribute('href')
        element.click()
        element_gallery = self.find_element((By.CSS_SELECTOR, ".mfp-img"))
        href_gallery = element_gallery.get_attribute('src')
        href_dict = {
            "1": href,
            "2": href_gallery
        }
        return href_dict

    def get_review_result(self):
        self.click_element((By.CSS_SELECTOR, 'a[href="#tab-review"]'))
        name = self.wd.find_element_by_id('input-name')
        name.send_keys('Oleg')
        review = self.wd.find_element_by_id('input-review')
        review.send_keys(self.text)
        self.click_element((By.CSS_SELECTOR,'input[name="rating"]:nth-child(5)'))
        self.click_element((By.CSS_SELECTOR, 'input[name="rating"]:nth-child(3)'))
        self.click_element((By.CSS_SELECTOR,'#button-review'))
        index = -1
        message = WebDriverWait(self.wd, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-success')
        return index
