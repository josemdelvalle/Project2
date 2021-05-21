from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The user is logged in')
def user_logs_on(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('G:/Project2/templates/login.html')
    context.login_page.username_input().send_keys("jose")
    context.login_page.password_input().send_keys("12345")
    context.login_page.login_button().click()
    sleep(1)


@given(u'The user is on the store page')
def user_on_store_page(context):
    print(context.driver.title)
    assert context.driver.title == "Store Page"


@when(u'The user clicks on a product')
def user_clicks_on_product(context):
    context.store_page.product().click()


@then(u'The user goes to that product\'s description page')
def user_on_item_overview_page(context):
    sleep(1)
    assert context.driver.title != "Store Page"
