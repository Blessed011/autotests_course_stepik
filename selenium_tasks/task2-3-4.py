from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/alert_accept.html"

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    value = browser.find_element(By.ID, 'input_value')
    x = value.text

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(func(x))

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    time.sleep(5)
    print(browser.switch_to.alert.text)
    browser.quit()