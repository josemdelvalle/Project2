from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The user is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('http:wikipedia.com')
    sleep(5)


@given(u'The user is on the menu page')
def step_impl(context):
    pass


@when(u'The user clicks on a product')
def step_impl(context):
    pass


@then(u'The user goes to that product\'s description page')
def step_impl(context):
    pass
