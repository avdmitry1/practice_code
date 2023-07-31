from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)')
    first_name.send_keys('Sergio')
    last_name = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)')
    last_name.send_keys('Ramos')
    email = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)')
    email.send_keys('Ramos@gmail.com')
    directory = 'D:/Python Project/practice_code/'
    file_name = 'coffee.txt'
    file_path = os.path.join(directory, file_name)
    upload = browser.find_element(By.CSS_SELECTOR, '#file')
    upload.send_keys(file_path)
    btn = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
finally:
    time.sleep(10)
browser.quit()