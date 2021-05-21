from selenium.webdriver.chrome.webdriver import WebDriver


class ProductPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_quantity_input(self):
        return self.driver.find_element_by_id("productQuantity")

    def get_cart_submit_button(self):
        return self.driver.find_element_by_id("addCartButton")

    def get_confirmation_text(self):
        return self.driver.find_element_by_id("confirmationText")
