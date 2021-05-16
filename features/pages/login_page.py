from selenium.webdriver.chrome.webdriver import WebDriver


class LoginHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_input(self):
        return self.driver.find_element_by_id("usernameInput")

    def password_input(self):
        return self.driver.find_element_by_id("passwordInput")

    def login_button(self):
        return self.driver.find_element_by_id("loginButton")
