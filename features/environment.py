from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginHomePage


def before_all(context):
    print("started")
    driver: WebDriver = webdriver.Chrome('C:/Users/JMDel/Documents/Revature/Selenium/chromedriver.exe')
    login_page = LoginHomePage(driver)
    context.driver = driver
    context.login_page = login_page


def after_all(context):
    context.driver.quit()
    print("ended")
