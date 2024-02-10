#Create a test case that will open the Target Circle page https://www.target.com/circle
# and verify there are 5 benefit boxes:


from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_GRID = (By.CSS_SELECTOR, "ul[class*='styles__BenefitsGrid-sc-9mx6dj-1 gXrXKV']")

@given('Open Target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(6)


@then('Verify benefits section grid has 5 boxes')
def verify_benefits_section(context):
    grid_links = context.driver.find_elements(*BENEFIT_GRID)
    print(len(grid_links))
# I was only able to obtain 1 element-waiting to get assistance if locator is correct


