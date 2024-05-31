from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
result = calc(x)
input2 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)

btn = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
time.sleep(10)
browser.quit()