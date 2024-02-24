from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class EmptyCartPage(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".styles__StyledHeading-sc-1xmf98v-0.lfA-Dem")

    def verify_empty_cart_message(self, cart_message):
        actual_message = self.find_element(*self.EMPTY_CART_MESSAGE).text
        assert cart_message in actual_message, f'Expected message {cart_message} but got {actual_message}'
        sleep(6)


