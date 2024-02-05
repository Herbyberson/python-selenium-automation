from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from time import sleep

@given('Target webpage opened')
def open_target_webpage(context):
    context.driver.get('https://www.target.com/')
    account_link = WebDriverWait(context.driver, 10).until(
    condition.element_o_be_clickable((By.XPATH, "//*[@data-test='@web/AccountLink']")))

    account_link.click()


@when('Sign out users click sign on')
def sign_in(context):
    context.driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()


@then('Verify sign in form is opened')
def verify_sign_in(context):
    text_shown = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text

    assert text_shown == actual_text
    sleep(5)
