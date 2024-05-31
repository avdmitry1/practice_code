from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y = browser.find_element(By.CSS_SELECTOR, '#num2').text
    res = int(x) + int(y)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(f'{str(res)}')
    btn = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
