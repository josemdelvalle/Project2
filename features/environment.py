from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginHomePage


def before_all(context):
    driver: WebDriver = webdriver.Chrome('C:/Users/marcl/chromedriver.exe')
    login_page = LoginHomePage(driver)
    context.driver = driver
    context.login_page = login_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
