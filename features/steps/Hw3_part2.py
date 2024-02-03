from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Target main page')
def step_impl(context):
    context.driver.get("https://www.target.com/")


@when('User click cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = '@web/CartLink']").click()
    sleep(6)


@then('Verify cart is empty')
def verify_cart(context):

    actual_text = context.driver.find_element(By.CSS_SELECTOR, '.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem').text
    assert 'Your cart is empty' in actual_text, f'Expected {actual_text} is not in {actual_text}'

    print("Test pass")

