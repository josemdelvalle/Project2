from time import sleep
from behave import when, given, then
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.cart_page import CartPage
from features.pages.login_page import LoginHomePage
from features.pages.store_page import StorePage


@given(u'The user is on the cart page')
def step_impl(context):
    store_page: StorePage = context.store_page
    sleep(5)
    store_page.get_cart_button().click()
    sleep(8)
    assert store_page.driver.title == "My Cart"


@given(u'The user has items in the cart')
def step_impl(context):
    cart_page: CartPage = context.cart_page
    assert cart_page.get_first_item_discard_button_by_name(169)


@when(u'The user clicks on remove order')
def step_impl(context):
    cart_page: CartPage = context.cart_page
    cart_page.get_first_item_discard_button_by_name(169).click()
    sleep(8)


@then(u'The item gets removed from the cart')
def step_impl(context):
    try:
        cart_page: CartPage = context.cart_page
        cart_page.get_first_item_discard_button_by_name(169)
        raise AssertionError
    except NoSuchElementException:
        assert True
