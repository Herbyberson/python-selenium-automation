from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text("coffee", *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

