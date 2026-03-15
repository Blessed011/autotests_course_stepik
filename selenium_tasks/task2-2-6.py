from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://SunInJuly.github.io/execute_script.html"
def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element(By.ID, 'input_value')
    x = value.text

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(func(x))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button.click()

finally:
    time.sleep(5)
    browser.quit()