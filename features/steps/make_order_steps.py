from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The user is on the order page')
def step_impl(context):
    pass


@when(u'The fills out an order')
def step_impl(context):
    pass


@then(u'The order gets added to the cart')
def step_impl(context):
    pass
