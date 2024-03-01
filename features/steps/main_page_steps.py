from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
VIEW_CART_PAGE = (By.XPATH, "//a[@href='/cart']")
ORDER_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-order-summary']")
SIDE_NAV_BRAND_NAME = (By.CSS_SELECTOR, "h4[class*='styles__StyledHeading']")
ORDER_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".styles__StyledHeading-sc-1xmf98v-0.lfA-Dem")


@given('Open Target main page')
def open_target_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search(context, product):
    context.app.header.search_product()
    context.app.header.click_search_button()


@when('log out users click Sign In')
def log_out_users_click_sign_in(context):
    context.app.header.click_sign_in_icon()


@then('Add to cart first result of product')
def add_to_cart_first_result(context):
    context.app.search_results_page.click_add_to_cart_button()
    context.app.search_results_page.click_add_to_cart_side_nav()


@when('log out users click Sign In on Side Navigation')
def log_out_users_click_signin_nav(context):
    context.app.header.side_nav_sign_in()


@then('Verify "{expected_message}" message')
def verify_expected_message(context, expected_message):
    context.app.sign_in_page.signin_message_verify()


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.app.header.click_cart_icon()


@then('Verify "{expected_text}" message is shown')
def verify_cart_message(context, expected_text):
    context.app.empty_cart_page.verify_empty_cart_message()
    sleep(6)


@then('Verify that every product has a name and an image')
def verify_product_name(context):
    # slowing down the browser to see all products
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(6)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)


@when('Click on Add to Cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(6)


@when('Store product name')
def store_product_name(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_BRAND_NAME))
    context.product_name = context.driver.find_element(*SIDE_NAV_BRAND_NAME).text


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BUTTON).click()
    sleep(6)


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*VIEW_CART_PAGE).click()


@then('Verify cart has {amount} item(s)')
def verify_cart_amount(context, amount):
    summary = context.driver.find_element(*ORDER_SUMMARY).text
    assert amount in summary, f"Expected 'empty cart', but got {summary}"


@then('Verify cart has correct product')
def verify_cart_product(context):
    actual_name = context.driver.find_element(*ORDER_NAME).text
    assert context.product_name == actual_name, f"Expected {context.product_name}, but got {actual_name}"
    sleep(10)
