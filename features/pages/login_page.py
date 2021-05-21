from selenium.webdriver.chrome.webdriver import WebDriver


class LoginHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def url(self):
        self.driver.get("http://127.0.0.1:5500/login.html")
        return self.driver.maximize_window()

    def username_input(self):
        return self.driver.find_element_by_id("usernameInput")

    def password_input(self):
        return self.driver.find_element_by_id("passwordInput")

    def login_button(self):
        return self.driver.find_element_by_id("loginButton")

    def customer_login(self):
        self.username_input().send_keys("jose")
        self.password_input().send_keys("12345")
        self.login_button().click()

