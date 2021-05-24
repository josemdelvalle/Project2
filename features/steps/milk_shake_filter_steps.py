from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.login_page import LoginHomePage
from features.pages.product_page import ProductPage
from features.pages.store_page import StorePage

@when(u'The user clicks on Milk Shake  filter')
def step_impl(context):
    context.store_page.get_milk_shake_filter_button().click()
    sleep(8)


@then(u'The Lists of products get filtered by Milk Shake')
def step_impl(context):
    assert len(context.store_page.get_all_product_cards()) < 18

