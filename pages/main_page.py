from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from random import choice
from .cart import Cart
from .utils import scroll_to_element


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.set_main_page()
        self.accept_cookie()
        self.header_links: dict[str, WebElement] = {}
        self.products: dict[str, WebElement] = {}

        self.update_header_links()

    def get_header_links(self) -> dict[str, WebElement]:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.top-nav__item")))
        links_list = list(filter(lambda x: x.accessible_name, self.driver.find_elements(By.CSS_SELECTOR, 'a.top-nav__item')))
        print(f"Получены ссылки из хедера: {', '.join(map(lambda x: x.accessible_name, links_list))}")

        return {
            link.accessible_name: link
            for link in links_list
        }

    def get_current_product_list(self):
        self.driver.implicitly_wait(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.product-tile"))
        )

        products: list[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, "a.product-tile")
        res_dict = {}
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, ".product-tile__name").text
            order_button = product.find_element(By.CSS_SELECTOR, ".product-tile__add-btn")
            res_dict[product_name] = order_button
        return res_dict

    def click_to_header(self, link_name: str, is_load_products=False):
        print(f"Кликаем на ссылку в хедере: {link_name}")
        link = self.header_links.get(link_name, False)
        if link:
            link.click()
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1.content-title"), link_name)
            )
            if is_load_products:
                self.update_products()
        else:
            print(f"Не найдена ссылка с именем {link_name} среди {self.header_links.keys()}")

    def click_to_order_button(self, product_name: str):
        print(f"Заказываем {product_name}")
        button = self.products.get(product_name, False)
        scroll_to_element(self.driver, button)
        if button:
            button.click()

        else:
            print(f"Не найден продукт с именем {product_name} среди {self.products.keys()}")

    def order_random_product(self):
        product = choice(list(self.products.keys()))
        self.click_to_order_button(product)

    def set_random_order(self, products_count=-1):
        if products_count == -1:
            for link_name in self.header_links.keys():
                self.click_to_header(link_name, is_load_products=True)
                self.order_random_product()
        else:
            pass



    def accept_cookie(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[4]/div/div[2]')))
            self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[4]/div/div[2]').click()
            print("Куки приняты")
        except Exception as e:
            pass

    def navigate_header(self, num):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 '//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/div[2]/nav/a')))
            elements = self.driver.find_elements(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/div[2]/nav/a'
            )
            # print(elements)
            elements[num].click()
        except Exception as e:
            print(f"No such element in header as {num} ", e)

    def navigate_footer(self, keyword):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 '//*[@id="app"]/div[2]/div[2]/div/nav/a')))
            element = self.driver.find_element(by=By.XPATH,
                                               value=f"//nav[@class='main-footer__bottom-nav']/a]")
            element.click()
        except Exception as e:
            print(f"No such element in footer as {keyword} ", e)

    def add_to_cart(self, number):
        # self.accept_cookie()
        elements = self.driver.find_elements(by=By.XPATH,
                                             value='//div[contains(@class, "bttn product-tile__add-btn bttn_primary")]')
        print(elements)
        try:
            elements[number].click()
            WebDriverWait(self.driver, 10).until(
                self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div/a').click())

        except Exception as e:
            print(f"No element with this number {number}", e)

    def learn_more(self, number):
        elements = self.driver.find_elements(by=By.CLASS_NAME, value="product-tile")
        try:
            elements[number].click()
        except Exception as e:
            print(f"No element with this number {number}", e)

    def update_header_links(self):
        self.header_links = self.get_header_links()

    def update_products(self):
        self.products = self.get_current_product_list()

    def set_main_page(self):
        self.driver.get("https://baranbellini.ru/")
        self.header_links = self.get_header_links()

    def go_to_cart(self):
        cart = Cart(self.driver)