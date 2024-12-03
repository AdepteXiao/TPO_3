from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time


def scroll_to_element(driver: WebDriver, element: WebElement, step=50, delay=0.3):
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    current_scroll_position = driver.execute_script("return window.pageYOffset;")

    last_position = driver.execute_script("return document.body.scrollHeight;")

    while current_scroll_position < last_position:
        if element.is_displayed():
            break

        driver.execute_script(f"window.scrollBy(0, {step});")
        time.sleep(delay)

        current_scroll_position = driver.execute_script("return window.pageYOffset;")

        last_position = driver.execute_script("return document.body.scrollHeight;")

    if element.is_displayed():
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1)
    else:
        print("Не удалось найти элемент на странице :(")
