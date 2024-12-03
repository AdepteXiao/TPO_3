import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage

@pytest.fixture(scope="class")
def setup():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    main_page = MainPage(driver)
    yield driver, main_page
    driver.quit()

class Test:
    @pytest.mark.usefixtures("setup")
    def test_0_cookie_accept(self, setup):
        driver = setup[0]
        main_page = MainPage(driver)
        cookies = driver.get_cookies()
        print(cookies)
        accepted = any(cookie["name"] == "cookies_accepted" and cookie["value"] == "true" for cookie in cookies)
        assert accepted

    # @pytest.mark.usefixtures("setup_without_main_page")
    # def test_0_1_cookie_accept(self, setup_without_main_page):
    #     driver = setup_without_main_page
    #     cookies = driver.get_cookies()
    #     print(cookies)
    #     accepted = any(cookie["name"] == "cookies_accepted" and cookie["value"] == "false" for cookie in cookies)
    #     assert accepted, "Куки приняты, а не должны были"
    #
    # @pytest.mark.usefixtures("setup_with_main_page")
    # def test_0_2_cookie_accept(self, setup_with_main_page):
    #     driver = setup_with_main_page[0]
    #     cookies = driver.get_cookies()
    #     print(cookies)
    #     accepted = any(cookie["name"] == "cookies_accepted" and cookie["value"] == "true" for cookie in cookies)
    #     assert accepted, "Куки не приняты, а должны были"

    @pytest.mark.usefixtures("setup")
    def test_1_1_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Горячее")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/main", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_2_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Мангал")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/grill", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_3_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Салаты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/salads", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_4_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Хинкали и манты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/khinkali_i_manty", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_5_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Выпечка")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/bakery", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_6_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Супы")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/soups", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_7_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Закуски")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/snacks", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_8_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Десерты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/sweets", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_9_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Бизнес-ланчи")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/lunch", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_10_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("На компанию")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/na_kompaniyu", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_11_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Баку")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/baku", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_12_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Полуфабрикаты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/semifinished", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_13_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Соусы")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/sauces", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup")
    def test_1_14_navigation_in_header(self, setup):
        driver, main_page = setup
        main_page.click_to_header("Напитки")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/drinks", "Страница не совпадает с заявленной"

    # def test_2_add_to_cart_from_main(self):
    #     self.driver.get("https://baranbellini.ru/")
    #     self.driver.implicitly_wait(10)
    #     self.main_page.add_to_cart(1)
    #
    # def t3_make_order(self):
    #     pass
