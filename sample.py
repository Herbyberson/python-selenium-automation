from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# path to chrome browser instance

driver_path = ChromeDriverManager().install()

# create instance of chrome browser

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)

#Open Target.com

driver.get('https://www.target.com/')

sleep(10)
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()




