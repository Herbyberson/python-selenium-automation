from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):

    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='shippingButton']")
    VIEW_CART_PAGE = (By.XPATH, "//a[@href='/cart']")

    def verify_search_results_correct(self, expected_result):
        self.verify_partial_text(expected_result, *self.SEARCH_RESULTS_HEADER)

    def verify_search_results_page_url(self, expected_part_url):
        self.verify_partial_url(expected_part_url)

    def click_add_to_cart_button(self):
        self.wait_element_clickable_click(*self.ADD_TO_CART_BUTTON)
        sleep(6)

    def click_add_to_cart_side_nav(self):
        self.wait_element_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BUTTON)

    def view_cart_page(self):
        self.wait_element_clickable_click(*self.VIEW_CART_PAGE)
        sleep(6)


