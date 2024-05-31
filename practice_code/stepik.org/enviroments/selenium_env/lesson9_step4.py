from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
alert = browser.switch_to.alert
alert.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
res = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(res)
btn = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
time.sleep(5)
browser.quit()