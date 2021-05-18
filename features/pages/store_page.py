from selenium.webdriver.chrome.webdriver import WebDriver
import random


class StorePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def product(self):
        return self.driver.find_element_by_id(random.randint(0, 22))
