from selenium.webdriver.chrome.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_first_item_discard_button_by_xpath(self):
        return self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[4]/button"
        )

    def get_submit_button(self):
        return self.driver.find_element_by_id("submitOrderBtn")

    def get_first_item_discard_button_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def get_submit_text_div(self):
        return self.driver.find_element_by_id("orderSubmitNotificationText")

    def get_cart_items(self):
        return self.driver.find_elements_by_class_name('cartItem')
