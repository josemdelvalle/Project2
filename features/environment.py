from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginHomePage
from features.pages.store_page import StorePage


def before_all(context):
    print("started")
    driver: WebDriver = webdriver.Chrome('G:/RevatureWork/SeleniumDrivers/chromedriver.exe')
    driver.implicitly_wait(2)
    login_page = LoginHomePage(driver)
    store_page = StorePage(driver)
    context.driver = driver
    context.login_page = login_page
    context.store_page = store_page


def after_all(context):
    # context.driver.quit()
    print("ended")
