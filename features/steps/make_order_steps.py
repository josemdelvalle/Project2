from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.login_page import LoginHomePage
from features.pages.product_page import ProductPage
from features.pages.store_page import StorePage


@given(u'The user is on the productOverview page')
def to_order_page(context):
    print("hello")
    context.store_page.get_random_product_by_name().click()
    sleep(7)


@when(u'The user fills out an order')
def step_impl(context):
    product_page: ProductPage = context.product_page
    sleep(5)
    product_page.get_quantity_input().clear()
    product_page.get_quantity_input().send_keys(5)
    sleep(5)
    product_page.get_quantity_input().clear()
    product_page.get_quantity_input().send_keys(2)
    sleep(5)


@when(u'The user clicks on the submit button')
def step_impl(context):
    product_page: ProductPage = context.product_page
    product_page.get_cart_submit_button().click()
    sleep(5)


@then(u'The order gets added to the cart')
def step_impl(context):
    product_page: ProductPage = context.product_page
    text = product_page.get_confirmation_text().text
    sleep(8)
    assert text == "Product added to cart!"
