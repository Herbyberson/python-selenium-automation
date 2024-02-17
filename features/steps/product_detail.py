from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open target {product_id} page')
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(6)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['micro chip', 'white', 'black']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.replace('color\n', '')
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected color {expected_colors} does not match {actual_colors}'

