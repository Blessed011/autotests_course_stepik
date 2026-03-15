from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    value = browser.find_element(By.ID, 'input_value')
    x = value.text

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(func(x))

    submit = browser.find_element(By.ID, 'solve')
    submit.click()

finally:
    time.sleep(3)
    browser.quit()