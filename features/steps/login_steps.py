from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The User is on the Project 1 LogIn Page')
def go_to_login_page(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('G:/Project2/templates/login.html')
    # sleep(5)


@when(u'The user types the jose in the username bar')
def input_username(context):
    context.login_page.username_input().send_keys("jose")


@when(u'The user types the 12345 in the password bar')
def input_password(context):
    context.login_page.password_input().send_keys("12345")


@when(u'Presses the login button')
def step_impl(context):
    context.login_page.login_button().click()


@then(u'The Logged in Logged in appears')
def step_impl(context):
    sleep(1)
    print(context.driver.title)
    assert context.driver.title == "Store Page"

