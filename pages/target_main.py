from selenium.webdriver.common.by import By
from time import sleep

from pages.Base_page import Page


class TargetMain(Page):

    def target_main(self):
        self.open('https://www.target.com')
        sleep(10)

