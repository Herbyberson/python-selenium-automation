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


# open the url
driver.get('https://www.target.com/')

sleep(5)

# connecting by ID
driver.find_element(By.CSS_SELECTOR, '#login')

# this is the same as

driver.find_element(By.ID, 'login')

# By class

driver.find_element(By.CSS_SELECTOR, '.styles__AuthInput-sc-q9vn5-0.eeoYPi')

# search by Tag

driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-link-inner')

# by attributes tag[attribute=value]

driver.find_element(By.CSS_SELECTOR,"[placeholder='Search Amazon']")

# by partial attributes *=

driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search']")

#from parent ---to child---separate by space

driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")

