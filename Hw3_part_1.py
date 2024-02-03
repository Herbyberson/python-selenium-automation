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

# finding locators using CSS selectors

# amazon logo

driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#Create account

driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')

#your name

driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# mobile number or email

driver.find_element(By.CSS_SELECTOR, '#ap_email')

#password

driver.find_element(By.CSS_SELECTOR, '#ap_password')

#reenter password

driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#continue button

driver.find_element(By.CSS_SELECTOR, '.a-button-input')

#condition of use

driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")

#privacy

driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")

#sign in link

driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")




