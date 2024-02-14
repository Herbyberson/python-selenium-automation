from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='shippingButton']")
VIEW_CART_PAGE = (By.XPATH, "//a[@href='/cart']")
ORDER_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-order-summary']")

@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(6)


@when('Click on Add to Cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(6)


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BUTTON).click()
    sleep(4)


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*VIEW_CART_PAGE).click()


@then('Verify cart has {amount} item(s)')
def verify_cart_amount(context, amount):
    summary = context.driver.find_element(*ORDER_SUMMARY).text
    assert amount in summary, f"Expected 'empty cart', but got {summary}"



