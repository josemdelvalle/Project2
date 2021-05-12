from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The User is on the Project 1 LogIn Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('http:google.com')
    print("Here------------------------------------")
    sleep(5)


@when(u'The user types the Robert in the username bar')
def step_impl(context):
    pass


@when(u'The user types the Stark in the password bar')
def step_impl(context):
    pass


@when(u'Presses the submit button')
def step_impl(context):
    pass


@then(u'The Logged in Logged in appears')
def step_impl(context):
    pass
