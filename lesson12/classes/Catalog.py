import time
from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Catalog(BasePage):


    def __init__(self, wd):
        self.wd = wd

    def get_count_elements(self):
        self.click_element((By.CSS_SELECTOR, "#list-view"))
        count_elements = self.wd.find_elements_by_class_name('product-layout')
        self.click_element((By.CSS_SELECTOR, "#grid-view"))
        count_elements1 = self.wd.find_elements_by_class_name('product-layout')
        len_dict = {
            "1": len(count_elements),
            "2": len(count_elements1)
        }
        return len_dict

    def get_attribute_first_letter(self):
        input_sort = Select(self.wd.find_element_by_id('input-sort'))
        input_sort.select_by_index(2)
        card = self.wd.find_elements_by_css_selector('.caption h4 > a')
        first_letter = card[0].get_attribute('innerHTML')
        return first_letter

    def get_clicked_url(self):
        self.click_element((By.CSS_SELECTOR, "#banner0"))
        url = self.wd.current_url
        return url

    def get_name_product(self):
        self.click_element((By.CSS_SELECTOR, ".list-group-item:nth-child(6)"))
        card = self.wd.find_elements_by_css_selector('.caption  h4 > a')
        card1 = card[0].get_attribute('innerHTML')
        return card1

    def get_text_message(self):
        self.click_element((By.CSS_SELECTOR, ".button-group button:nth-child(2)"))
        message = WebDriverWait(self.wd, 2).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ".alert a")))
        name_card = message[2].get_attribute('innerHTML')
        return name_card
