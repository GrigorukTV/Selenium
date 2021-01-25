import logging
from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Catalog(BasePage):

    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, ".product-layout")
    GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    INPUT_SORT = (By.CSS_SELECTOR, "#input-sort")
    CAPTION_H4 = (By.CSS_SELECTOR, ".caption h4 > a")
    BANNER0 = (By.CSS_SELECTOR, "#banner0")
    LIST_GROUP_ITEM = (By.CSS_SELECTOR, ".list-group-item:nth-child(6)")
    BUTTON_GROUP = (By.CSS_SELECTOR, ".button-group button:nth-child(2)")
    ALERT = (By.CSS_SELECTOR, ".alert a")
    log_path = "logs/Catalog.log"

    def get_count_elements(self):
        self.click_element(self.LIST_VIEW)
        count_elements = self.find_elements(self.PRODUCT_LAYOUT)
        self.click_element(self.GRID_VIEW)
        count_elements1 = self.find_elements(self.PRODUCT_LAYOUT)
        len_dict = {
            "1": len(count_elements),
            "2": len(count_elements1)
        }
        return len_dict

    def get_attribute_first_letter(self):
        input_sort = Select(self.find_element(self.INPUT_SORT))
        input_sort.select_by_index(2)
        card = self.find_elements(self.CAPTION_H4)
        first_letter = card[0].get_attribute('innerHTML')
        return first_letter

    def get_clicked_url(self):
        self.click_element(self.BANNER0)
        url = self.wd.current_url
        return url

    def get_name_product(self):
        self.click_element(self.LIST_GROUP_ITEM)
        card = self.find_elements(self.CAPTION_H4)
        card1 = card[0].get_attribute('innerHTML')
        return card1

    def get_text_message(self):
        self.click_element(self.BUTTON_GROUP)
        message = self.elements_located(self.ALERT)
        name_card = message[2].get_attribute('innerHTML')
        return name_card
