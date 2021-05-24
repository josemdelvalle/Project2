from selenium.webdriver.chrome.webdriver import WebDriver
import random


class StorePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_random_product_by_name(self):
        return self.driver.find_element_by_name(random.randint(0, 22))

    def get_product_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def get_cart_button(self):
        return self.driver.find_element_by_id("cartBtn")
