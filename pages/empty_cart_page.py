from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class EmptyCartPage(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".styles__StyledHeading-sc-1xmf98v-0.lfA-Dem")

    def verify_empty_cart_message(self):
        expected_text = 'Your cart is empty'
        self.wait_element_visible(*self.EMPTY_CART_MESSAGE)
        self.verify_text(expected_text, *self.EMPTY_CART_MESSAGE)

        sleep(6)


