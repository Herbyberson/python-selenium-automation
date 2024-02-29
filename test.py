
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Start chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com
driver.get('https://www.target.com/')

# Wait for the AccountLink element to be clickable
account_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@data-test='@web/AccountLink']"))
)

# Click on the AccountLink
account_link.click()

# Add any additional code for signing in, if needed
# For example:
# driver.find_element(By.ID, "username").send_keys("your_username")
# driver.find_element(By.ID, "password").send_keys("your_password")
# driver.find_element(By.ID, "submit_button").click()

# Optionally, add a sleep to visually inspect the changes on the page
sleep(5)

# Close the browser
driver.quit()