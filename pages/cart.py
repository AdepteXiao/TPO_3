from selenium.webdriver.common.by import By
from .utils import scroll_to_element

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.product_list = list[dict()]()
        self.get_products_list()

    def finish_order(self):
        try:
            order_button = self.driver.find_element(by=By.CLASS_NAME, value="bttn_bigger")
            scroll_to_element(self.driver, order_button)
            order_button.click()
        except Exception as e:
            print("Не удалось оформить заказ", e)

    def get_products_list(self):
        try:
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
            print(cart_items)
            for item in cart_items:
                name_element = item.find_element(By.CLASS_NAME, "cart-item__product-name")
                name = name_element.text if name_element else "Unknown"

                amount_element = item.find_element(By.CLASS_NAME, "counter-changer__value")
                amount = amount_element.text if amount_element else "0"

                price_element = item.find_element(By.CLASS_NAME, "cart-item__price")
                price = price_element.text.replace("₽", "").strip() if price_element else "0"


                self.product_list.append({
                    "name": name,
                    "amount": amount,
                    "price": price
                })
            return self.product_list
        except Exception as e:
            print("Все сломалось, можно вешаться ", e)


    def change_tableware_amount(self, way='inc'):
        parent_container = self.driver.find_element(By.CLASS_NAME, "cart-page-complementary-products__cutlery")
        if way == 'inc':
            btn = parent_container.find_elements(by=By.CLASS_NAME, value='counter-changer__btn_inc')[-1]
        else:
            btn = parent_container.find_elements(by=By.CLASS_NAME, value='counter-changer__btn_dec')[-1]
        scroll_to_element(self.driver, btn)
        btn.click()


    def change_product_amount(self, num=0, way='inc'):
        try:
            elements = self.driver.find_elements(by=By.CLASS_NAME, value='counter-changer__btn_inc') if way == 'inc' else self.driver.find_elements(by=By.CLASS_NAME, value='counter-changer__btn_dec')
            elements[num].click()
        except Exception as e:
            print("Не удалось изменить количество товара", e)

    def delete_from_cart(self, num=0):
        try:
            elements = self.driver.find_elements(by=By.CLASS_NAME, value='cart-item__remostore')
            element = elements[num].find_element(by=By.CLASS_NAME, value='cris-cross')
            scroll_to_element(self.driver, element)
            element.click()
        except Exception as e:
            print("Не удалось удалить товар из корзины", e)

    def change_tableware_need(self):
        try:
            parent = self.driver.find_element(by=By.CLASS_NAME, value='cart-page-complementary-products__cutlery-needed')
            element = parent.find_element(by=By.CLASS_NAME, value='checkbox-custom__checkmark')
            scroll_to_element(self.driver, element)
            element.click()
        except Exception as e:
            print("Не удалось изменить флаг", e)