from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def finish_order(self):
        try:
            finish_order_path = '//*[@id="app"]/div[1]/main/div[1]/div/div[5]/div[3]/div[2]/div/button'
            self.driver.find_element(by=By.XPATH, value=finish_order_path).click()
            print("Заказ оформлен")
        except Exception as e:
            print("Не удалось оформить заказ", e)
            pass

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