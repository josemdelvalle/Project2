from selenium.webdriver.chrome.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def remove_first_item(self):
        return self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[4]/button"
        )

    def get_submit_button(self):
        return self.driver.find_element_by_id("submitOrderBtn")
