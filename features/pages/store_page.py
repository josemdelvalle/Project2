from selenium.webdriver.chrome.webdriver import WebDriver
import random


class StorePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_random_product_by_name(self):
        return self.driver.find_element_by_name(random.randint(1, 13))

    def get_product_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def get_cart_button(self):
        return self.driver.find_element_by_id("cartBtn")

    def get_ice_cream_filter_button(self):
        return self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/button")

    def get_milk_shake_filter_button(self):
        return self.driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/button")

    def get_all_product_cards(self):
        return self.driver.find_elements_by_class_name("productCard")
