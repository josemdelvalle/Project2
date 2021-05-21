from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.login_page import LoginHomePage
from features.pages.product_page import ProductPage
from features.pages.store_page import StorePage


@given(u'The user is on the order page')
def to_order_page(context):
    login: LoginHomePage = context.login_page
    login.driver.implicitly_wait(2)
    login.url()
    login.customer_login()
    sleep(2)


@when(u'The user fills out an order')
def step_impl(context):
    store_page: StorePage = context.store_page
    product_page: ProductPage = context.product_page

    store_page.get_product_by_id(4).click()
    sleep(2)

    product_page.driver.implicitly_wait(2)
    product_page.get_quantity_input().send_keys(2)
    product_page.get_cart_submit_button().click()


@then(u'The order gets added to the cart')
def step_impl(context):
    product_page: ProductPage = context.product_page
    text = product_page.get_confirmation_text().text
    assert text == "Product added to cart!"
