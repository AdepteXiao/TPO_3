from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.product_list = []
        self.get_products_list()

    def finish_order(self):
        try:
            finish_order_path = '//*[@id="app"]/div[1]/main/div[1]/div/div[5]/div[3]/div[2]/div/button'
            self.driver.find_element(by=By.XPATH, value=finish_order_path).click()
            print("Заказ оформлен")
        except Exception as e:
            print("Не удалось оформить заказ", e)

    def get_products_list(self):
        try:
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart-item")

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


    def add_tableware(self):
        self.driver.find_element(by=By.CLASS_NAME, value='counter-changer__btn_inc').click()

    def subtract_tableware(self):
        self.driver.find_element(by=By.CLASS_NAME, value='counter-changer__btn_dec').click()

    def add_product_amount(self, num):
        elements = self.driver.find_elements(by=By.XPATH, value='//button[contains(@class, "counter-changer__btn counter-changer__btn_inc")')
        elements[num].click()

    def add_random_meal_amount(self):

        pass


    def delete_from_cart(self):
        pass