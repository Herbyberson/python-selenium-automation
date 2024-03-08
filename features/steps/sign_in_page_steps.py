from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.main_page.open_main()
    context.app.header.click_sign_in_icon()
    context.app.header.side_nav_sign_in()
    sleep(5)


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle
    print('current window', context.original_window)


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.Sign_in_page.click_terms_condition()
    sleep(5)


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.Sign_in_page.switch_to_new_window()
    print('After switching to a new window:')
    print('All windows:', context.driver.window_handles)
    print('Current window', context.driver.current_window_handle)


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.Sign_in_page.verify_terms_conditions_url()


@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.Sign_in_page.switch_to_window_by_id(context.original_window)
    print('After switching to original window:', context.driver.current_window_handle)


def close(context):
    context.driver.close()
    sleep(10)
