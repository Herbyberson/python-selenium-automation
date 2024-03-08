from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignIn(Page):
    SIGNIN_MESSAGE = (By.CSS_SELECTOR, ".styles__StyledHeading-sc-1xmf98v-0.styles__AuthHeading-sc-kz6dq2-2.jhKFiw.kcHdEa")
    TERM_MESSAGE = (By.CSS_SELECTOR, "[target='_blank']")

    def signin_message_verify(self):
        expected_text = 'Sign into your Target account'
        self.wait_element_visible(*self.SIGNIN_MESSAGE)
        self.verify_text(expected_text, *self.SIGNIN_MESSAGE)

    def click_terms_condition(self):
        self.wait_element_clickable_click(*self.TERM_MESSAGE)

    def verify_terms_conditions_url(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions/-/N-4sr7l')
