from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    res = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(res)
    btn = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    input2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    input2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций