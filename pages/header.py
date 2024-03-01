from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BUTTON = (By.XPATH, "//a[@aria-label='Account, sign in']")
    SIDE_NAV_SIGNIN_BUTTON = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    ORDER_SUMMARY = (By.XPATH, "//h4[@class='styles__StyledHeading-sc-1xmf98v-0 dQsNJZ']")

    def search_product(self):
        self.input_text("Stanley Cup", *self.SEARCH_FIELD)

    def click_sign_in_icon(self):
        self.wait_element_clickable_click(*self.SIGN_IN_BUTTON)

    def side_nav_sign_in(self):
        self.wait_element_clickable_click(*self.SIDE_NAV_SIGNIN_BUTTON)

    def click_search_button(self):
        self.wait_element_clickable_click(*self.SEARCH_ICON)
        sleep(6)

    def verify_product_info(self):
        self.verify_partial_text(*self.ORDER_SUMMARY)
        sleep(6)

