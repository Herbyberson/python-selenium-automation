from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BUTTON = (By.XPATH, "//a[@aria-label='Account, sign in']")
    SIDE_NAV_SIGNIN_BUTTON = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def search_product(self):
        self.input_text("coffee", *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_sign_in_icon(self):
        self.wait_element_clickable_click(*self.SIGN_IN_BUTTON)

    def side_nav_sign_in(self):
        self.wait_element_clickable_click(*self.SIDE_NAV_SIGNIN_BUTTON)
