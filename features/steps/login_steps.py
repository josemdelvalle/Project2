from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The user is on the login home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get('https://www.wikipedia.org/')
    sleep(1)


@when(u'The user inputs their username into the username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user inputs their username into the username field')


@when(u'The user inputs their password into the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user inputs their password into the password field')


@when(u'The user clicks on the login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user clicks on the login button')


@then(u'The user should login successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user should login successfully')
