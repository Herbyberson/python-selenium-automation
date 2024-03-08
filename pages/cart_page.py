from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(Page):

    PRODUCT_NAME = (By.CSS_SELECTOR, ".styles__StyledLink-sc-vpsldm-0.ifDhat.h-display-block.h-text-md")

    def verify_product_description(self):
        self.verify_partial_text(*self.PRODUCT_NAME)

