# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
#
# from features.pages.trms_home_page import TRMSHomePage
#
#
# def before_all(context):
#     driver: WebDriver = webdriver.Chrome('C:/Users/marcl/chromedriver.exe')
#     driver.implicitly_wait(2)
#     trms_home_page = TRMSHomePage(driver)
#     context.driver = driver
#     context.trms_home_page = trms_home_page
#     print("started")
#
#
# def after_all(context):
#     context.driver.quit()
#     print("ended")


from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginHomePage


# All setup and teardown functions must go in this file.
# These functions must be named using behave's conventions
def before_all(context):
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver: WebDriver = webdriver.Chrome('C:/Users/marcl/chromedriver.exe')
    login_page = LoginHomePage(driver)
    context.driver = driver
    context.login_page = login_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
