from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.cart_page import CartPage
from features.pages.login_page import LoginHomePage
from features.pages.store_page import StorePage


@given(u'The user has items in the cart')
def step_impl(context):
    pass


@given(u'The user is on the cart page')
def step_impl(context):
    login: LoginHomePage = context.login_page
    store_page: StorePage = context.store_page

    login.url()
    store_page.get_cart_button().click()

    assert store_page.driver.title == "My Cart"


@when(u'The user clicks on remove order')
def step_impl(context):
    cart_page: CartPage = context.store_page
    cart_page.remove_first_item().click()


@then(u'The item gets removed from the cart')
def step_impl(context):
    assert True
    # need some sort of confirmation here
