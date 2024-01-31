
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
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
    condition.element_to_be_clickable((By.XPATH, "//*[@data-test='@web/AccountLink']"))
)

# Click on the AccountLink
account_link.click()

#click sign in
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()


text_shown = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text

assert text_shown == actual_text
sleep(5)