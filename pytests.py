import time
from itertools import product

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pages.cart import Cart
from pages.main_page import MainPage

# TODO: объединить тесты test_1_...
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage


@pytest.fixture(scope="class")
def setup_1():
    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    cart = Cart(driver)
    main_page = MainPage(driver, cart)
    yield driver, main_page, cart
    driver.quit()

@pytest.fixture(scope="class")
def setup_2():
    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    cart = Cart(driver)
    main_page = MainPage(driver, cart)
    main_page.set_random_order(1)
    driver.get("https://baranbellini.ru/cart")
    driver.implicitly_wait(10)
    yield driver, cart
    driver.quit()

@pytest.fixture(scope="class")
def setup_without_main_page():
    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


class TestCookies:
    @pytest.mark.usefixtures("setup_1")
    def test_0_1_cookie_accept(self, setup_1):
        driver = setup_1[0]
        time.sleep(1)
        cookies = driver.get_cookies()
        accepted = any(cookie["value"] == "true" for cookie in cookies)
        assert accepted, "Куки не приняты, а должны были быть"

    @pytest.mark.usefixtures("setup_without_main_page")
    def test_0_2_cookie_accept(self, setup_without_main_page):
        driver = setup_without_main_page
        driver.get("https://baranbellini.ru/")
        time.sleep(1)
        cookies = driver.get_cookies()
        assert (cookies == [] or any(
            cookie["value"] == "false" for cookie in cookies)), "Куки приняты, а не должны были быть"

class TestHeaderNavigation:
    @pytest.mark.usefixtures("setup_1")
    def test_1_1_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Горячее")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/main", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_2_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Мангал")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/grill", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_3_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Салаты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/salads", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_4_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Хинкали и манты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/khinkali_i_manty", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_5_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Выпечка")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/bakery", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_6_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Супы")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/soups", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_7_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Закуски")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/snacks", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_8_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Десерты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/sweets", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_9_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Бизнес-ланчи")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/lunch", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_10_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("На компанию")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/na_kompaniyu", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_11_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Баку")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/baku", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_12_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Полуфабрикаты")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/semifinished", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_13_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Соусы")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/sauces", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_1_14_navigation_in_header(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_header("Напитки")
        main_page.get_current_product_list()
        assert driver.current_url == "https://baranbellini.ru/drinks", "Страница не совпадает с заявленной"

class TestCart:
    @pytest.mark.usefixtures("setup_1")
    def test_2_1_adding_to_cart(self, setup_1):
        driver, main_page, cart = setup_1
        products_ordered = main_page.set_random_order()
        driver.get("https://baranbellini.ru/cart")
        driver.implicitly_wait(10)
        prods_in_cart = [p["name"] for p in cart.get_products_list()]
        assert products_ordered == prods_in_cart, "Продукты в корзине не совпадают с заказанными"

    @pytest.mark.usefixtures("setup_2")
    def test_2_2_increasing_amount_in_cart(self, setup_2):
        driver, cart = setup_2
        amount_before = driver.find_element(by=By.CLASS_NAME, value='counter-changer__value').text
        cart.change_product_amount(0, 'inc')
        amount_after = driver.find_element(by=By.CLASS_NAME, value='counter-changer__value').text
        assert int(amount_before) + 1 == int(amount_after), "Количество товара не увеличилось"

    @pytest.mark.usefixtures("setup_2")
    def test_2_3_decreasing_amount_in_cart(self, setup_2):
        driver, cart = setup_2
        cart.change_product_amount(0, 'inc')
        amount_before = driver.find_element(by=By.CLASS_NAME, value='counter-changer__value').text
        cart.change_product_amount(0, 'dec')
        amount_after = driver.find_element(by=By.CLASS_NAME, value='counter-changer__value').text
        assert int(amount_before) - 1 == int(amount_after), "Количество товара не увеличилось"

    @pytest.mark.usefixtures("setup_2")
    def test_2_4_returning_product_to_cart(self, setup_2):
        driver, cart = setup_2
        cart.delete_from_cart()
        driver.find_element(by=By.CLASS_NAME, value='cart-item__restore').click()
        driver.refresh()
        cart_list = driver.find_elements(by=By.CLASS_NAME, value='cart-item')
        assert cart_list != [], "Товар удален из корзины"

    @pytest.mark.usefixtures("setup_2")
    def test_2_5_deleting_product_in_cart(self, setup_2):
        driver, cart = setup_2
        cart.delete_from_cart()
        driver.refresh()
        cart_list = driver.find_elements(by=By.CLASS_NAME, value='cart-item')
        assert cart_list == [], "Товар не удален из корзины"

class TestFinishingOrder:
    @pytest.mark.usefixtures("setup_2")
    def test_3_1_finishing_order_w_tableware(self, setup_2):
        driver, cart = setup_2
        cart.change_tableware_amount('inc')
        cart.finish_order()
        assert driver.current_url == "https://baranbellini.ru/order", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_2")
    def test_3_2_finishing_order_wo_tableware(self, setup_2):
        driver, cart = setup_2
        driver.get("https://baranbellini.ru/cart")
        cart.change_tableware_need()
        cart.finish_order()
        assert driver.current_url == "https://baranbellini.ru/order", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_2")
    def test_3_3_err_finishing_order_wo_tableware(self, setup_2):
        driver, cart = setup_2
        driver.get("https://baranbellini.ru/cart")
        cart.finish_order()
        assert driver.current_url != "https://baranbellini.ru/order", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_2")
    def test_3_4_err_finishing_order_w_empty_cart(self, setup_2):
        driver, cart = setup_2
        driver.get("https://baranbellini.ru/cart")
        cart.change_tableware_need()
        cart.delete_from_cart()
        cart.finish_order()
        assert driver.current_url != "https://baranbellini.ru/order", "Страница не совпадает с заявленной"

class TestFooterNavigation:
    @pytest.mark.usefixtures("setup_1")
    def test_4_1_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Акции")
        assert driver.current_url == "https://baranbellini.ru/promo", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_4_2_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Доставка и оплата")
        assert driver.current_url == "https://baranbellini.ru/delivery-and-payment", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_4_3_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Контакты")
        assert driver.current_url == "https://baranbellini.ru/contacts", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_4_4_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Зоны доставки")
        assert driver.current_url == "https://baranbellini.ru/delivery-zones", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_4_5_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Правовая информация")
        assert driver.current_url == "https://baranbellini.ru/legal-information", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_4_6_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Бонусная программа")
        assert driver.current_url == "https://baranbellini.ru/loyalty-program", "Страница не совпадает с заявленной"

    @pytest.mark.usefixtures("setup_1")
    def test_4_7_navigation_in_footer(self, setup_1):
        driver, main_page = setup_1[:-1]
        main_page.click_to_footer("Работа в Bellini")
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://hr.bellinigroup.ru/", "Страница не совпадает с заявленной"