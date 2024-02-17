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


