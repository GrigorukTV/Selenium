from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By

class CatalogId(BasePage):
    text = 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    IMAGE_ADD = (".image-additional")
    H2 = (By.CSS_SELECTOR, ".list-unstyled h2")
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    CART_TOTAL = (By.CSS_SELECTOR, 'cart-total')
    THUMBNAIL = (By.CSS_SELECTOR, '.thumbnails .thumbnail')
    MFP_IMG = (By.CSS_SELECTOR, ".mfp-img")
    A_HREF = (By.CSS_SELECTOR, 'a[href="#tab-review"]')
    INPUT_NAME = (By.CSS_SELECTOR, '#input-name')
    INPUT_REVIEW = (By.CSS_SELECTOR, '#input-review')
    RATING_CHILD_5 = (By.CSS_SELECTOR, 'input[name="rating"]:nth-child(5)')
    RATING_CHILD_3 = (By.CSS_SELECTOR, 'input[name="rating"]:nth-child(3)')
    BUTTON_REVIEW = (By.CSS_SELECTOR, '#button-review')
    ALERT = (By.CLASS_NAME, "alert")
    log_path = "logs/CatalogId.log"

    def get_len_elements(self):
        return self.return_len(self.IMAGE_ADD)

    def get_price(self):
        element = self.find_element(self.H2)
        price = element.get_attribute('innerHTML')
        price = float(price.replace('$', ''))
        return price

    def get_number_product(self):
        self.click_element(self.BUTTON_CART)
        self.text_present(self.CART_TOTAL,'0 item(s) - $0.00')
        el = self.self.find_element(self.CART_TOTAL)
        cart = el.get_attribute('innerHTML')
        index = cart.find('1 item')
        return index

    def get_url_gallery(self):
        element = self.find_element(self.THUMBNAIL)
        href = element.get_attribute('href')
        element.click()
        element_gallery = self.find_element(self.MFP_IMG)
        href_gallery = element_gallery.get_attribute('src')
        href_dict = {
            "1": href,
            "2": href_gallery
        }
        return href_dict

    def get_review_result(self):
        self.click_element(self.A_HREF)
        self.send_keys(self.INPUT_NAME, "Oleg")
        review = self.find_element(self.INPUT_REVIEW)
        review.send_keys(self.text)
        self.click_element(self.RATING_CHILD_5)
        self.click_element(self.RATING_CHILD_3)
        self.click_element(self.BUTTON_REVIEW)
        index = -1
        message = self.element_located(self.ALERT)
        if message is not None:
            cl_message = message.get_attribute('class')
            index = cl_message.find('alert-success')
        return index
