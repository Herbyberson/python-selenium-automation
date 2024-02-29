from selenium.webdriver.common.by import By
from time import sleep

from pages.Base_page import Page


class CirclePage(Page):
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")

    def open_circle(self):
        self.open('https://www.target.com/circle')
        sleep(10)

    def verify_can_click_thru_tabs(self):
        # making sure tabs are ready to be clicked
        self.wait_element_clickable(*self.BONUS_TAB)

        tabs = self.find_elements(*self.TABS)
        current_url = ''

        for i in range(len(tabs)):
            # Search for tabs before every click to avoid StaleElementReferenceException
            tabs = self.find_elements(*self.TABS)
            tabs[i].click()

            sleep(7)

            # self.wait_url_changes(current_url)
            # current_url = self.driver.current_url
