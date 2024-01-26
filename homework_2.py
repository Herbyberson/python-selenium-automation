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


# open the url
driver.get('https://www.amazon.com/ap/signin

sleep(5)

# populate for Amazon logo

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# populate Email field

driver.find_element(By.XPATH, "//input[@type='email']")

# continue button
driver.find_element(By.XPATH, "//input[@id='continue']" )

# conditions of use link

driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']"
)

# privacy notice link

driver.find_element(By.XPATH,"//a[@href='/gp/aw/help/ref=ap_mobile_signin_notification_privacy_notice?id=468496>Privacy Notice</a>']")

# need help link

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")




