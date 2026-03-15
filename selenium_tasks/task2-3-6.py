from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/redirect_accept.html"

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element(By.ID, 'input_value')
    x = value.text

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(func(x))

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    print(browser.switch_to.alert.text)
    time.sleep(5)
    browser.quit()