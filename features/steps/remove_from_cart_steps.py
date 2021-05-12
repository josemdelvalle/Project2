from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The user has items in the cart')
def step_impl(context):
    pass


@given(u'The user is on the cart page')
def step_impl(context):
    pass


@when(u'The user clicks on remove order')
def step_impl(context):
    pass


@then(u'The item gets removed from the cart')
def step_impl(context):
    pass
