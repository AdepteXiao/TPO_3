from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


class Tests:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.main_page = MainPage(self.driver)
        self.is_order_set_up = False

    # def test_set_up_order(self):
    #     self.main_page.set_random_order()
    #     self.is_order_set_up = True
    #
    # def test_0_click_to_link_in_header(self):
    #     self.main_page.click_to_header("Соусы")
    #     self.main_page.get_current_product_list()

    def test_1_1_navigation_in_header(self):
        self.main_page.click_to_header("Горячее")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_2_navigation_in_header(self):
        self.main_page.click_to_header("Мангал")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_3_navigation_in_header(self):
        self.main_page.click_to_header("Салаты")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_4_navigation_in_header(self):
        self.main_page.click_to_header("Хинкали и манты")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_5_navigation_in_header(self):
        self.main_page.click_to_header("Выпечка")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_6_navigation_in_header(self):
        self.main_page.click_to_header("Супы")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_7_navigation_in_header(self):
        self.main_page.click_to_header("Закуски")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_8_navigation_in_header(self):
        self.main_page.click_to_header("Десерты")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_9_navigation_in_header(self):
        self.main_page.click_to_header("Бизнес-ланчи")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_10_navigation_in_header(self):
        self.main_page.click_to_header("На компанию")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_11_navigation_in_header(self):
        self.main_page.click_to_header("Баку")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_12_navigation_in_header(self):
        self.main_page.click_to_header("Полуфабрикаты")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_13_navigation_in_header(self):
        self.main_page.click_to_header("Соусы")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    def test_1_14_navigation_in_header(self):
        self.main_page.click_to_header("Напитки")
        self.main_page.get_current_product_list()
        assert self.driver.current_url == ""

    # def test_2_add_to_cart_from_main(self):
    #     self.driver.get("https://baranbellini.ru/")
    #     self.driver.implicitly_wait(10)
    #     self.main_page.add_to_cart(1)
    #
    # def t3_make_order(self):
    #     pass
