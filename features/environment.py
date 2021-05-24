from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.cart_page import CartPage
from features.pages.login_page import LoginHomePage
from features.pages.store_page import StorePage
from features.pages.product_page import ProductPage


def before_all(context):
    print("started")
    driver: WebDriver = webdriver.Chrome('C:/Users/JMDel/Documents/Revature/Selenium/chromedriver.exe')
    driver.implicitly_wait(2)
    login_page = LoginHomePage(driver)
    store_page = StorePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    context.driver = driver
    context.login_page = login_page
    context.store_page = store_page
    context.cart_page = cart_page
    context.product_page = product_page


def after_all(context):
    # context.driver.quit()
    print("ended")
