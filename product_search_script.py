# Practice with Locators

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Navigate to Target.com

driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('coffee')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

# allow time pass to find element due to add
sleep(6)

expected_word = 'coffee'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

assert expected_word == actual_text, f'Expected word {actual_text}, not in {actual_text}'

