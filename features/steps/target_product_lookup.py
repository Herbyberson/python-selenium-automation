#Update Target product search test case and add Behave variables.

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
RESULT_MESSAGE = (By.XPATH, "//div[@data-test='resultsHeading']")

@given('Open Target')
def open_target_main_page(context):
    context.driver.get("https://www.target.com/")


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(6)


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    actual_text = context.driver.find_element(*RESULT_MESSAGE).text
    assert expected_result in actual_text, f" expected_result {expected_result} not in {actual_text}"


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f"Expected {expected_part_url} not in {url} "

