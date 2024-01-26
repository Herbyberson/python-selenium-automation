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

# populate search field
search = driver.find_element(By.ID, "What can we help you find? suggestions appear below")

search.clear()
search.send_keys('table')

# wait for 4 sec
sleep(4)

driver.find_element(By.XPATH,"//input[@aria-label='Search Amazon']")