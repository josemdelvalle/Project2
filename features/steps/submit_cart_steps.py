from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.cart_page import CartPage
from features.pages.login_page import LoginHomePage


@when(u'The user clicks on submit order')
def step_impl(context):
    cart_page: CartPage = context.cart_page
    cart_page.get_submit_button().click()


@then(u'The item gets submitted')
def step_impl(context):
    assert True
    # need some sort of confirmation for this test
