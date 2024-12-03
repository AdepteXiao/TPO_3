from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)

# Инициализация драйвера
driver = webdriver.Chrome()

driver.get("https://baranbellini.ru")  # Замените на URL вашей страницы


def get_header_links(driver) -> dict[str, WebElement]:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.top-nav__item")))

    # Поиск элемента по CSS-селектору
    return {
        link.accessible_name: link
        for link in filter(lambda x: x.accessible_name, driver.find_elements(By.CSS_SELECTOR, 'a.top-nav__item'))
    }


links = get_header_links(driver)

for key, value in links.items():
    print(f"Открываем {key}")
    value.click()

driver.quit()
