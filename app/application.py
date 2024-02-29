from pages.Base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.empty_cart_page import EmptyCartPage
from pages.circle_page import CirclePage
from pages.target_main import TargetMain
from pages.Sign_in_page import SignIn

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.empty_cart_page = EmptyCartPage(driver)
        self.circle_page = CirclePage(driver)
        self.target_page = TargetMain(driver)
        self.sign_in_page = SignIn(driver)



