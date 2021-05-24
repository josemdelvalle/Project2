from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.login_page import LoginHomePage


@given(u'The User is on the LogIn Page')
def go_to_login_page(context):
    login: LoginHomePage = context.login_page
    login.url()
    sleep(5)


@when(u'The user types the {username} in the username bar')
def input_username(context, username):
    context.login_page.username_input().send_keys(username)
    sleep(5)


@when(u'The user types the {password} in the password bar')
def input_password(context, password):
    context.login_page.password_input().send_keys(password)
    sleep(5)


@when(u'Presses the login button')
def step_impl(context):
    context.login_page.login_button().click()
    sleep(5)


@then(u'Redirected to Store Page')
def step_impl(context):
    print(context.driver.title)
    assert context.driver.title == "Store Page"
